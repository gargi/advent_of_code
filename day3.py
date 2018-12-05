#!/usr/bin/env python
from collections import defaultdict
lines = open('day3_input.txt').read().split('\n')
overlap = defaultdict(int)
for line in lines:
    parts = line.split()
    if parts:
        claim = parts[0]
        left, top = parts[2].split(",")
        left, top = int(left), int(top[:-1])
        width, height = parts[3].split("x")
        width, height = int(width), int(height)
        for i in range(width):
            for j in range(height):
                overlap[(left+i, top+j)] += 1
ans = 0
for k, v in overlap.items():
    if v >= 2:
        ans += 1
print(ans)

# Part 2
for line in lines:
    parts = line.split()
    if parts:
        claim = parts[0]
        left, top = parts[2].split(",")
        left, top = int(left), int(top[:-1])
        width, height = parts[3].split("x")
        width, height = int(width), int(height)
        non_overlap = True
        for i in range(width):
            for j in range(height):
                if overlap[(left+i, top+j)] >= 2:
                    non_overlap = False
        if non_overlap:
            print(claim)
