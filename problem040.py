#! /usr/bin/python3

def digit(n):
    if n < 10:
        return n
    n -= 10
    
    width = 2
    amount = 90
    start_value = 10
    while True:
        if n < width*amount:
            return int(str(start_value + int(n/width))[n%width])
        n -= width*amount
        
        width += 1
        amount *= 10
        start_value *= 10
    
product = 1
for i in range(7):
    product *= digit(10**i)
print(product)
