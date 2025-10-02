#!/usr/bin/env python3
import sys

for line in sys.stdin:
    num = line.strip()
    if num:
        print(f"{num}\t1")