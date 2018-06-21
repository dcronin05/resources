def gcdRecur(a, b):

    return max(a, b) if a and b == 0 else gcdRecur(min(a, b), max(a, b) % min(a, b))

print(gcdRecur(555, 728949))
