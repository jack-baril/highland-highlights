#!/bin/sh

set -e

cd highland-highlights

if ! find assets/documents -type f -name "*.docx" | grep -q .; then
  printf 'Error: No DOCX file found in "assets/documents".'
  exit 1
fi

if ! find assets/documents -type f -name "*.pdf" | grep -q .; then
  printf 'Error: No PDF file found in "assets/documents".'
  exit 1
fi

. .venv/bin/activate
python3 src/main.py
