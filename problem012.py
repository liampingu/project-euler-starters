#! /usr/bin/python3

# prints first triangle number to have over 5 divisors

# is it efficient? to find all the divisors of 100, do you really need to test
# 51, 52, 53 ... 100? Do you really need to test anything over 10?

def number_of_divisors(x):
    count = 0
    for divisor in range(1, x+1):
        if x % divisor == 0:
            count += 1
    return count
    
number = 1
triangle_number = 1

while True:
    if number_of_divisors(triangle_number) > 5:
        break
    
    number += 1
    triangle_number += number
    
print(triangle_number)
