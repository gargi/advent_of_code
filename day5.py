#!/usr/bin/env python
import sys
input = open('day5_input.txt').read().strip()
#input="dabAcCaCBAcCcaDA"
alpha = {}
rest = "abcdefghijklmnopqrstuvwxyz"
for i in range(97,123):
    alpha[chr(i)] = chr(i-32)
for i in range(65,91):
    alpha[chr(i)] = chr(i+32)

def part1(input):
    st = []
    for char in input:
        if st:
            top = st.pop()
            if top == alpha.get(char):
                continue
            else:
                st.append(top)
                st.append(char)
        # Stack is empty
        else:
            st.append(char)
    return len(st)

def part2():
    min_len = sys.maxint
    for i in rest:
        input1 = [l for l in input if l != i and l != alpha.get(i)]
        curr_len = part1(input1)
        min_len = min(min_len, curr_len)
    print(min_len)

result = part1(input)
print(result)

part2()
