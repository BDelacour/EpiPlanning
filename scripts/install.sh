#!/bin/bash

CURRENT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "${CURRENT_DIR}/.."
rm -rf .venv
virtualenv --no-site-packages .venv
source .venv/bin/activate
pip install -r "scripts/requirements.txt" $*
