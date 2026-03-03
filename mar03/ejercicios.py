def mean3(a, b, c):
    return (a + b + c) / 3

def max3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def min3(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
print(mean3(1, 2, 3))
print(max3(1, 2, 3))
print(min3(1, 2, 3))