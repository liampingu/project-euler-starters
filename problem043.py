#! /usr/bin/python3

total = 0

def substr_int(x, offset):
    return int(''.join(x[offset:offset+3]))

def test(x):
    if  substr_int(x,1) % 2 == 0 and \
        substr_int(x,2) % 3 == 0 and \
        substr_int(x,3) % 5 == 0 and \
        substr_int(x,4) % 7 == 0 and \
        substr_int(x,5) % 11 == 0 and \
        substr_int(x,6) % 13 == 0 and \
        substr_int(x,7) % 17 == 0:
            return True
    return False
    
def iterate(selected, remaining):
    if len(remaining) == 0:
        if test(selected):
            global total
            total += int(''.join(selected))
    else:
        for i in range(len(remaining)):
            selected_copy = selected.copy()
            remaining_copy = remaining.copy()
            selected_copy.append(remaining_copy.pop(i))
            iterate(selected_copy, remaining_copy)
            
            
remaining = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
iterate([], remaining)
print(total)
