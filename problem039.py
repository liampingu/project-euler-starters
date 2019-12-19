#! /usr/bin/python3

import math

max_count = 0
max_p = 120

for p in range(121, 1001):
    count = 0
    for a in range(1, math.ceil(p/3)):
        for b in range(a, math.ceil(p/2)):
            c = p - a - b
            if a**2 + b**2 == c**2:
                count += 1
    if count > max_count:
        print('p={} ==> count={}'.format(p, count))
        max_count = count
        max_p = p
        
print(p)
