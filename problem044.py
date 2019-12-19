#! /usr/bin/python3

import math

# nth pentagonal number
def P(n):
    return (3*n*n-n)/2

# inverse function
def N(p):
    n = math.floor((1 + math.sqrt(1 + 24*p))/6)
    if P(n) == p:
        return n
    return None

# main
n_diff = 1400
while True:
    print('trying n_diff = {}'.format(n_diff))
    p_diff = P(n_diff)
    
    n_small = 1
    while True:
        p_small = P(n_small)
        
        p_big = p_small + p_diff
        if p_big < P(n_small+1):
            break
        n_big = N(p_big)
        if n_big == None:
            n_small += 1
            continue
            
        p_sum = p_big + p_small
        n_sum = N(p_sum)
        if n_sum != None:
            print('diff:  P({}) ==> {}'.format(n_diff, p_diff))
            print('small: P({}) ==> {}'.format(n_small, p_small))
            print('big:   P({}) ==> {}'.format(n_big, p_big))
            print('sum:   P({}) ==> {}'.format(n_sum, p_sum))
            exit()
            
        n_small += 1
        
    n_diff += 1
        
    
