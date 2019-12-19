
import math

# size of largest square that fits under y+y0 = 1/(x+x0)
def square(x0, y0):
    b = x0 + y0
    c = x0*y0 - 1.0
    return (-b + math.sqrt(b**2 - 4.0*c)) / 2.0

# follow 'RUU' style string to get size of square found by going right, up then up
def get_size(directions, x0, y0):
    s = square(x0, y0)
    if len(directions) == 0:
        return s
    if directions.pop(0) == 'U':
        return get_size(directions, x0, y0+s)
    return get_size(directions, x0+s, y0)

# count num squares smaller than s0 that fit under y+y0 = 1/(x+x0)
def count(s0, x0, y0):
    s = square(x0, y0)
    if s < s0:
        return 0
    return 1 + count(s0, x0, y0+s) + count(s0, x0+s, y0)
    
def result():
    s0 = get_size(list('RRRUUU'), 1.0, 0.0)
    return count(s0, 1.0, 0.0)
