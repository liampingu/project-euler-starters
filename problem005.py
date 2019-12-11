#! /usr/bin/python3

# prints smallest number divisible by all integers from 1 to 10 inclusive

# is this efficient? it seems there could be a better way to go about this.
# also, it seems to keep testing for divisibility after one test fails.

number = 1

while True:

    divisible_by_all = True
    for factor in range(1, 10+1):
        if number % factor != 0:
            divisible_by_all = False
            
    if divisible_by_all:
        break
        
    number += 1
    
print(number)
