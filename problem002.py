#! /usr/bin/python3

# prints sum of even fibonacci numbers under 100

previous_num = 1
current_num = 2
total = 0

while current_num <= 100:

    if current_num % 2 == 0:
        total += current_num
        
    next_num = previous_num + current_num
    previous_num = current_num
    current_num = next_num
    
print(total)

