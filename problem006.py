#! /usr/bin/python3

# prints the difference between the square of the sum, and the sum of the square,
# of the first 10 natural numbers

# is this efficient? it seems to do the same loop twice

sum_of_squares = 0
for num in range(1, 10+1):
    sum_of_squares += num**2
    
square_of_sum = 0
for num in range(1, 10+1):
    square_of_sum += num
square_of_sum = square_of_sum**2

print(square_of_sum - sum_of_squares)
