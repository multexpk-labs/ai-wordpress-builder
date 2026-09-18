#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
[ -d .venv ] || { echo 'Run ./setup.sh first.'; exit 1; }
. .venv/bin/activate
python scripts/elementor.py "$@"
