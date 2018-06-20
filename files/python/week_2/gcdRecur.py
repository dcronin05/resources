def gcdRecur(a, b):

    return max(a, b) if a, b == 0 else gcdRecur(min(a, b), max(a, b) % min(a, b))

print(gcdRecur(42, 72))
