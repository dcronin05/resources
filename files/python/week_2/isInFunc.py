def isIn(char, aStr):

    if not aStr or len(aStr) == 1:
        return char == aStr
    else:

        if char >= aStr[len(aStr)//2]:
            return isIn(char, aStr[len(aStr)//2:])
        else:
            return isIn(char, aStr[:len(aStr)//2])


print(isIn('w', 'abcdefghijklmopqrstuvwxyz'))
