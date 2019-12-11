#! /usr/bin/python3

# prints product of pythagorean triplets whose elements sum to 1000

# is this efficient? it seems to check the 3-4-5 triplet 6 times!
# (3-4-5, 3-5-4, 4-3-5, 4-5-3, 5-3-4, 5-4-3)

def get_answer():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a*b*c
    return None
    
answer = get_answer()
print(answer)
