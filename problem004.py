#! /usr/bin/python3

# prints largest palindromic multiple of two 2 digit numbers

# is this efficient? it seems to test things twice (12 * 34 and 34 * 12)

def is_palindromic(number):
    string_forwards = str(number)
    string_backwards = string_forwards[::-1]
    if string_forwards == string_backwards:
        return True
    return False

largest = 0

for x in range(10, 100):
    for y in range(10, 100):
        if is_palindromic(x*y) and x*y > largest:
            largest = x*y
            
print(largest)       
