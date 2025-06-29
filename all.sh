#!/bin/sh

python scripts/fetch_csv.py
./scripts/copy_csv.sh
python scripts/generate_html.py
./scripts/copy_html.sh