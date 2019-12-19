#! /usr/bin/python3

import math

def tri(n):
    return n*n + n
    
def pent(n):
    return 3*n*n - n
    
def hexa(n):
    return 4*n*n - 2*n
    
t = 285 + 1
p = 165
h = 143

T = tri(t)
P = 0
H = 0

while True:
    if P < T:
        p += 1
        P = pent(p)
    if H < T:
        h += 1
        H = hexa(h)
    while T < P or T < H:
        t += 1
        T = tri(t)
    if T == P and T == H:
        print(int(T))
        break

