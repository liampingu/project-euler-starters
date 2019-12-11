#! /usr/bin/python3

# prints sum of number numbers less than 10 that are multiples of 3 or 5

total = 0

for number in range(10):
    if number % 3 == 0 or number % 5 == 0:
        total += number
        
print(total)
