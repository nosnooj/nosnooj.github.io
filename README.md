# nosnooj.github.io — 백엔드 개발자 포트폴리오

손준혁 · 백엔드 개발자 · 데이터 흐름 설계.
콘텐츠를 단일 소스로 모델링하고 템플릿으로 결정론적 빌드하는 경량 정적 사이트입니다.

**라이브:** https://nosnooj.github.io

라이트/다크 토글, 모바일 반응형, 케이스 스터디 도면 라이트박스(확대 보기), 이력서 PDF·Word 다운로드를 제공합니다.

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
│   ├── js/zoom.js               # 도면 라이트박스(확대 보기)
│   ├── diagrams/                # 케이스 스터디 SVG 도면 (빌드 시 HTML 인라인)
│   ├── img/profile.jpg          # 증명사진
│   └── files/                   # 이력서 PDF·DOCX (다운로드 대상)
├── requirements.txt
├── dev.sh                       # 빌드 + 로컬 미리보기 서버
└── .github/workflows/deploy.yml # main push → 빌드 → Pages 자동 배포
```

## 라우트

| 경로 | 페이지 |
|---|---|
| `/` | 표지 + Work 인덱스 + About (스크롤) |
| `/work/gaia/` | CS1 — Microarray LIMS · 결과지 자동화 (GAIA) |
| `/work/less/` | CS2 — LIS–ERP 연동 (LESS) |
| `/work/aws/` | CS3 — 온프레미스 → AWS 전환 |
| `/work/cos/` | CS4 — B2B 주문·정산 (COS) |
| `/work/ib/` | CS5 — B2C 영양제 추천 (IB) |

## 로컬 실행

```bash
pip install -r requirements.txt
python build.py                       # dist/ 생성
python -m http.server -d dist 8000    # http://localhost:8000
```

## 브랜치 워크플로

- **`develop`** — 작업·로컬 테스트용. 여기에 push해도 **배포되지 않는다**.
- **`main`** — 배포용. push되면 GitHub Actions가 자동 빌드·배포한다.

```bash
# 작업
git checkout develop
# ...편집...
./dev.sh                 # 빌드 + http://localhost:8000 미리보기
git add -A && git commit -m "작업 내용"
git push                 # develop 백업 (배포 안 됨)

# 배포: develop → main PR(Squash & merge) → Actions 자동 배포
# 머지 후 develop를 main에 재정렬
git checkout develop
git reset --hard main
git push --force-with-lease
```

## 배포

`main` 브랜치에 push하면 GitHub Actions가 빌드 후 GitHub Pages로 배포합니다.
저장소 **Settings → Pages → Source: GitHub Actions** 로 설정하세요.
워크플로는 `main` push에만 반응하므로 `develop` 작업은 배포에 영향을 주지 않습니다.

## 콘텐츠 수정

모든 문구·성과·프로젝트 내용은 `data/content.py` 한 곳에서 수정합니다. 케이스 스터디는 각 프로젝트의 `problem`·`decisions`·`build`·`result`, 이력서 다운로드는 `resumes[]`, 증명사진은 `profile_photo`를 수정하면 전 페이지에 반영됩니다.
