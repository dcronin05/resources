def isIn(char, aStr):

    if not aStr or len(aStr) == 1:
        return char == aStr
    else:
        return aStr[0] == char if char == aStr[0] else isIn(char, aStr[1:])


print(isIn('h', 'bcdefg'))
