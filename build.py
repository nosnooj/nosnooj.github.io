#!/usr/bin/env python3
"""
정적 사이트 빌더 — 콘텐츠(data/) + 템플릿(templates/) → dist/

설계 의도
- 콘텐츠는 data/content.py 단일 소스. 모든 페이지가 여기서만 데이터를 읽는다.
- 템플릿은 Jinja2. 표현(HTML/CSS)과 콘텐츠를 분리한다.
- 케이스 스터디는 PRD의 정보 구조대로 각자 별도 경로(/work/<slug>/)로 출력한다.
- 아키텍처 SVG는 빌드 시 인라인하고, 내부 색상 변수를 페이지 테마(data-theme)에
  연동해 라이트/다크 수동 토글에도 도면이 함께 반응하도록 변환한다.

결정론적 빌드: 같은 입력 → 같은 출력. 외부 런타임 상태 없음(정적 호스팅 적합).
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
# 출력 경로는 BUILD_OUT로 재정의 가능 (기본 dist/)
DIST = Path(os.environ.get("BUILD_OUT", ROOT / "dist")).resolve()
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"
DIAGRAMS = ASSETS / "diagrams"

import sys
sys.path.insert(0, str(ROOT))
from data import content  # noqa: E402


# ---------------------------------------------------------------------------
# SVG 인라인 + 테마 변수 변환
# ---------------------------------------------------------------------------
def _parse_var_block(css_body: str) -> dict[str, str]:
    """'--a:#fff;--b:#000' → {'--a':'#fff', '--b':'#000'}"""
    out: dict[str, str] = {}
    for decl in css_body.split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        name, _, value = decl.partition(":")
        out[name.strip()] = value.strip()
    return out


def inline_diagram(svg_path: Path) -> tuple[str, str]:
    """
    SVG를 인라인 가능한 형태로 변환한다.

    반환: (themed_svg_markup, diagram_css)
    - SVG 내부 <style>(자체 라이트값 + @media dark)를 제거하고,
      모든 var(--x)를 var(--d-x)로 네임스페이스 처리한다.
    - 라이트/다크 팔레트는 페이지의 [data-theme]에 묶인 CSS로 반환해,
      페이지 테마 토글이 SVG 색까지 제어하도록 한다.
    """
    svg = svg_path.read_text(encoding="utf-8")

    # 1) <style> 추출
    m = re.search(r"<style>(.*?)</style>", svg, flags=re.DOTALL)
    light: dict[str, str] = {}
    dark: dict[str, str] = {}
    if m:
        style_body = m.group(1)
        # 라이트: 첫 svg{...}
        lm = re.search(r"svg\s*\{([^}]*)\}", style_body)
        if lm:
            light = _parse_var_block(lm.group(1))
        # 다크: @media prefers-color-scheme:dark 내부 svg{...}
        dm = re.search(
            r"@media[^{]*prefers-color-scheme\s*:\s*dark[^{]*\{\s*svg\s*\{([^}]*)\}",
            style_body,
            flags=re.DOTALL,
        )
        if dm:
            dark = _parse_var_block(dm.group(1))
        # <style> 제거
        svg = svg[: m.start()] + svg[m.end():]

    # 2) var(--x) → var(--d-x) 네임스페이스
    svg = re.sub(r"var\(--([A-Za-z0-9_-]+)\)", r"var(--d-\1)", svg)
    # marker id 등 fill="var(--navy)"도 위 치환에 포함됨

    # 3) 페이지 테마에 묶인 변수 CSS 생성
    def block(selector: str, vars_map: dict[str, str]) -> str:
        decls = "".join(f"--d-{k.lstrip('-')}:{v};" for k, v in vars_map.items())
        return f"{selector}{{{decls}}}"

    diagram_css = ""
    if light:
        diagram_css += block(":root,[data-theme=light]", light)
    if dark:
        diagram_css += block("[data-theme=dark]", dark)

    # 반응형: 인라인 SVG가 가로폭에 맞게 축소되도록 보장
    svg = svg.replace("<svg ", '<svg style="width:100%;height:auto;display:block" ', 1)
    return svg, diagram_css


# ---------------------------------------------------------------------------
# 렌더링
# ---------------------------------------------------------------------------
def build() -> None:
    # 기존 산출물 정리 — 루트 디렉터리는 보존하고 내용만 비운다
    # (네트워크/FUSE 마운트에서 루트 rmdir이 막히는 경우 대응)
    if DIST.exists():
        for child in DIST.iterdir():
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                child.unlink()
    else:
        DIST.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    site = content.SITE
    projects = content.PROJECTS

    # 도면 인라인 (CS별 figures에 file 지정 시 로드)
    diagram_css_chunks: list[str] = []
    for proj in projects:
        for fig in proj.get("figures", []):
            if fig.get("file"):
                svg_markup, css = inline_diagram(DIAGRAMS / fig["file"])
                fig["svg"] = svg_markup
                if css:
                    diagram_css_chunks.append(css)
    diagram_css = "".join(dict.fromkeys(diagram_css_chunks))  # 중복 제거, 순서 유지

    common = dict(site=site, projects=projects, diagram_css=diagram_css)

    # 홈 — 사이트 루트 기준 상대경로 "./"
    # (root 변수를 모든 내부 링크·에셋 앞에 붙여, 루트/하위경로 어디에 배포돼도 동작)
    home_html = env.get_template("home.html").render(**common, page_id="home", root="./")
    (DIST / "index.html").write_text(home_html, encoding="utf-8")

    # 케이스 스터디 (각자 별도 경로 work/<slug>/, 루트까지 "../../")
    cs_tmpl = env.get_template("case_study.html")
    n = len(projects)
    for i, proj in enumerate(projects):
        prev_p = projects[i - 1] if i > 0 else None
        next_p = projects[i + 1] if i < n - 1 else None
        html = cs_tmpl.render(
            **common,
            page_id=proj["id"],
            project=proj,
            prev=prev_p,
            next=next_p,
            root="../../",
        )
        out_dir = DIST / "work" / proj["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")

    # 정적 에셋 복사 (css, js, pdf) — diagrams는 인라인하므로 복사 생략 가능하나 보존
    shutil.copytree(ASSETS, DIST / "assets")

    # Jekyll 비활성 (밑줄 폴더/경로 보존)
    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    pages = ["index.html"] + [f"work/{p['slug']}/index.html" for p in projects]
    print(f"빌드 완료 → {DIST}")
    for pg in pages:
        print(f"  - {pg}")


if __name__ == "__main__":
    build()
