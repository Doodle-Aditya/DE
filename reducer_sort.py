#!/usr/bin/env python3
import sys
current_num = None
for line in sys.stdin:
    num ,_ = line.strip().split("\t")
    if current_num != num:
        current_num=num
        print(num)