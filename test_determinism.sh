#!/bin/sh
# Determinism check: main.py must write byte-identical entry.txt on every run.
set -eu
cd "$(dirname "$0")"
rm -rf /tmp/bp-run1 /tmp/bp-run2
OUTPUT_DIR=/tmp/bp-run1 python3 main.py
OUTPUT_DIR=/tmp/bp-run2 python3 main.py
cmp /tmp/bp-run1/entry.txt /tmp/bp-run2/entry.txt
cmp /tmp/bp-run1/entry.txt entry.txt
python3 -c "s=open('entry.txt',encoding='utf-8').read(); assert 1 <= len(s) <= 200, len(s); assert s.strip() and '\n' not in s; print('entry.txt OK:', len(s), 'chars,', len(s.encode('utf-8')), 'bytes')"
echo "determinism OK"
