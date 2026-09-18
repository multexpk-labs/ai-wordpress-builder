#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
command -v python3 >/dev/null || { echo 'python3 is required'; exit 1; }
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
mkdir -p backup audit projects tests
touch backup/.gitkeep audit/.gitkeep projects/.gitkeep tests/.gitkeep
chmod +x setup.sh audit.sh backup.sh inspect-elementor.sh scripts/*.py 2>/dev/null || true
python scripts/audit.py --self-test
echo 'Setup complete. Configure .env before connecting to WordPress.'
