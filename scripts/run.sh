#!/bin/sh

set -e

cd highland-highlights
[ -z "$VIRTUAL_ENV" ] && . .venv/bin/activate
python3 highland-highlights/main.py
