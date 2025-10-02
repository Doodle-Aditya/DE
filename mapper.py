#!/usr/bin/env python3
import sys 
import re

WORD_RE = re.compile(r"\w+")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    words = WORD_RE.findall(line.lower())
    for word in words:
        print(f"{word}\t1")