#! /usr/bin/python3

import math

def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def test(selected):
    num = int(''.join([str(x) for x in selected]))
    if is_prime(num):
        print(num)
        exit()

def iterate(selected, remaining):
    if len(remaining) == 0:
        test(selected)
    else:
        for i in range(len(remaining)):
            selected_copy = selected.copy()
            remaining_copy = remaining.copy()
            selected_copy.append(remaining_copy.pop(i))
            iterate(selected_copy, remaining_copy)

remaining = [9, 8, 7, 6, 5, 4, 3, 2, 1]
while True:
    iterate([], remaining)
    remaining.pop(0)
