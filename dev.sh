#!/usr/bin/env bash
# 로컬 개발 미리보기 — 빌드 후 dist/를 로컬 서버로 띄운다.
# 사용: ./dev.sh   (Ctrl+C 로 종료)
set -e
cd "$(dirname "$0")"
python3 build.py
echo ""
echo "→ http://localhost:8000   (Ctrl+C 로 종료)"
python3 -m http.server -d dist 8000
