from random import randint
# n = input('You are in the Lost Forest. Go left or right?')
n = 'right'

aNumStr1 = 'hello'
print(len(aNumStr1))
aNumStr2 = 'big'
print(len(aNumStr2))
aNumStr3 = 'carries'
print(len(aNumStr3))

num = 0

try:
    while n == 'right':
        print("The count is ", num)
        num += 1
        exitNumber = randint(0,999999)
        print('The random number is ', exitNumber)
        for i in range(len(aNumStr2), len(aNumStr3)):
            print(len(aNumStr2), len(aNumStr3))
            print(i)
            print(aNumStr1)
        if exitNumber == 20:
            break

except:
    print('fucked up!')