#! /usr/bin/python3

# prints largest prime factor of 13195

# is this efficient? there seems to be a lot of unnecessary divisibility testing,
# both in the is_prime() function and the main code.

num = 13195

def is_prime(x):
    if x < 2:
        return False
    for factor in range(2, x):
        if x % factor == 0:
            return False
    return True

largest_factor = 1

for i in range(1, num):
    if num % i == 0 and is_prime(i):
        largest_factor = i
        
print(largest_factor)
