def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a <= b:
        if b % a == 0:
            return a
        for i in range(a, 0, -1):
            if b % i == 0 and a % i == 0:
                return i

    if a >= b:
        if a % b == 0:
            return b
        for i in range(b, 0, -1):
            if b % i == 0 and a % i == 0:
                return i


print(gcdIter(122342343, 2352))
