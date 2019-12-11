#! /usr/bin/python3

# prints sum of primes below 10

# is this efficient? have you heard of the sieve of erathosthenes method for
# finding lots of primes?

def is_prime(x):
    if x < 2:
        return False
    for factor in range(2, x):
        if x % factor == 0:
            return False
    return True
    
total = 0

for number in range(10):
    if is_prime(number):
        total += number
        
print(total)
