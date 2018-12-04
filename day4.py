#!/usr/bin/env python
from collections import defaultdict
lines = open('day4_input.txt').read().split('\n')
lines.sort()

guard_sleep = defaultdict(int)
best_min = defaultdict(int)

for line in lines:
    if line:
        words = line.split()
        date, time = words[0][1:],words[1][:-1]
        time_min = int(time.split(":")[1])
        #print(time_min)
    if "begins" in line:
        guard = words[3][1:]
    if "falls" in line:
        start = time_min
    if "wakes" in line:
        end = time_min
        guard_sleep[guard] += end-start
        for t in range(start, end):
            best_min[(guard, t)] += 1
#print(best_min)

# Part 1
max_value = 0
guard = None
for key, value in guard_sleep.items():
    if value > max_value:
        max_value = value
        guard = key
print(guard)

max_min_count = 0
max_min = 0
for key, value in best_min.items():
    if key[0] == guard:
        if value > max_min_count:
            max_min_count = value
            max_min = key[1]
print(guard, max_min)
print(max_min*int(guard))

# Part 2
max_count = 0
for key, value in best_min.items():
    if value > max_count:
        max_count = value
        max_2_min = key[1]
        guard = key[0]
print(guard, max_2_min)
print(int(guard)*max_2_min)
