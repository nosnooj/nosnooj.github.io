# nosnooj.github.io — 백엔드 개발자 포트폴리오

손준혁 · 백엔드 개발자 · 데이터 흐름 설계.
콘텐츠를 단일 소스로 모델링하고 템플릿으로 결정론적 빌드하는 경량 정적 사이트입니다.

## 설계 원칙

- **콘텐츠 단일 소스** — 모든 페이지는 `data/content.py` 한 곳에서만 데이터를 읽습니다. 문구·성과 수정은 이 파일만 고치면 전 페이지에 반영됩니다.
- **표현/콘텐츠 분리** — Jinja2 템플릿(`templates/`)이 HTML·CSS를, 데이터가 내용을 담당합니다.
- **정적 호스팅 적합** — 서버 런타임 상태 없이 같은 입력이면 같은 출력. GitHub Pages에 바로 배포됩니다.
- **테마 연동 도면** — 아키텍처 SVG는 빌드 시 인라인되며, 내부 색상 변수를 페이지 테마(`data-theme`)에 묶어 라이트/다크 토글에 함께 반응합니다.

## 구조

```
portfolio/
├── build.py                     # 빌드: 데이터+템플릿 → dist/, SVG 인라인·테마 변환
├── data/content.py              # 콘텐츠 단일 소스 (프로필·프로젝트·About)
├── templates/
│   ├── base.html                # 공통 레이아웃(topbar·footer·테마·SEO)
│   ├── home.html                # 표지 + Work + About (한 페이지)
│   └── case_study.html          # 케이스 스터디 공통 템플릿
├── assets/
│   ├── css/style.css            # 블루프린트 테마 토큰 (라이트/다크)
│   ├── js/theme.js              # 테마 토글(localStorage 영속)
│   ├── diagrams/cs1_arch.svg    # CS1 시스템 아키텍처 도면
│   └── pdf/                      # 이력서 PDF (업로드 후 content.py에 경로 지정)
├── requirements.txt
└── .github/workflows/deploy.yml # push → 빌드 → Pages 자동 배포
```

## 라우트

| 경로 | 페이지 |
|---|---|
| `/` | 표지 + Work 인덱스 + About (스크롤) |
| `/work/lims/` | CS1 — Microarray LIMS · 결과지 자동화 |
| `/work/less/` | CS2 — LIS–ERP 연동 (LESS) |
| `/work/cos/` | CS3 — B2B 주문·정산 (COS) |
| `/work/ib/` | CS4 — B2C 영양제 추천 (IB) |
| `/work/aws/` | CS5 — 온프레미스 → AWS 전환 |

## 로컬 실행

```bash
pip install -r requirements.txt
python build.py                       # dist/ 생성
python -m http.server -d dist 8000    # http://localhost:8000
```

## 배포

`main` 브랜치에 push하면 GitHub Actions가 빌드 후 GitHub Pages로 배포합니다.
저장소 **Settings → Pages → Source: GitHub Actions** 로 설정하세요.

## 콘텐츠 채우기

CS2~CS5는 현재 인덱스 카드 + 골격만 있고 본문은 비어 있습니다(이력서 작성 진행에 맞춰 채울 예정).
`data/content.py`의 해당 프로젝트 `problem`·`decisions`·`build`·`result`를 채우면 자동 반영됩니다.
