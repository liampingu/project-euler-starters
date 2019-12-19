
import math

# largest square to fit under x0,y0 curve: y+y0 = 1/(x+x0)
cdef double square(double x0, double y0) except *:
    cdef double b = x0 + y0
    cdef double c = x0*y0 - 1.0
    return (-b + math.sqrt(b**2 - 4.0*c)) / 2.0

# follow 'RUU' style string to get size of square found by going right, up then up
cdef double get_size(directions, double x0, double y0) except *:
    cdef double s = square(x0, y0)
    if len(directions) == 0:
        return s
    if directions.pop(0) == 'U':
        return get_size(directions, x0, y0+s)
    return get_size(directions, x0+s, y0)
    
# num of squares smaller than s0 that fit under x0,y0 curve, only moving *right*
cdef int count_tail(int depth, double s0, double x0, double y0) except *:
    cdef double s
    cdef int total = 0
    cdef int above = 1
    while above > 0:
        s = square(x0, y0)
        if s < s0:
            return total
        above = count_tail(depth+1, s0, x0, y0+s)
        total += above + 1
        x0 += s
    while True:
        s = square(x0, y0)
        if s < s0:
            return total
        total += 1
        x0 += s
    return total
    
# function accessible from python interpreter...
cpdef int result() except *:
    cdef double s0 = get_size(list('RRRUUU'), 1.0, 0.0)
    return count_tail(0, s0, 1.0, 0.0)
