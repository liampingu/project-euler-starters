
import math

# largest square to fit under x0,y0 curve: y+y0 = 1/(x+x0)
def square(x0, y0):
    b = x0 + y0
    c = x0*y0 - 1.0
    return (-b + math.sqrt(b**2 - 4.0*c)) / 2.0

# follow 'RUU' style string to get size of square found by going right then up
def get_size(directions, x0, y0):
    s = square(x0, y0)
    if len(directions) == 0:
        return s
    if directions.pop(0) == 'U':
        return get_size(directions, x0, y0+s)
    return get_size(directions, x0+s, y0)
    
# num of squares smaller than s0 that fit under x0,y0 curve
def count_squares(s0, x0, y0):
    s = square(x0, y0)
    total = 0
    while s > s0:
        above = count_squares(s0, x0, y0+s)
        if above == 0:
            break
        total += 1 + above
        x0 += s
        s = square(x0, y0)
    while s > s0:
        total += 1
        x0 += s
        s = square(x0, y0)
    return total

s0 = get_size(list('RRRUUU'), 1.0, 0.0)
print(1 + count_squares(s0, 1.0, 0.0))
