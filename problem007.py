#! /usr/bin/python3

# prints 6th prime number

# is this efficient? have you heard of the sieve of erathosthenes method for
# finding lots of primes?

def is_prime(x):
    if x < 2:
        return False
    for factor in range(2, x):
        if x % factor == 0:
            return False
    return True

number = 2
prime_count = 0

while True:
    if is_prime(number):
        prime_count += 1
        if prime_count == 6:
            break
    number += 1
    
print(number)
