#! /usr/bin/python3

import math

def is_triangle_number(value):
    value *= 2
    root = int(math.sqrt(value))
    if root * (root + 1) == value:
        return True
    return False

with open('problem042-words.txt', 'r') as f:
    words = [x for x in f.read().split('","')]
words[0] = words[0][1:]
words[-1] = words[-1][:-1]

count = 0
for word in words:
    value = sum([ord(x)-64 for x in word])
    if is_triangle_number(value):
        print(word)
        count += 1
print(count)
