x = 298374551329387429384729837423523
epsilon = 0.0000000001
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
regAns = round(float(format(ans**2, 'f')))
if round(ans)**2 == x:
    ans = round(ans)
    print('The square root of', x, 'is', ans)
else:
    print(ans, 'is close to square root of', x, '\n', ans, 'cubed is', regAns)
    print("The difference is", format(x-ans**2, '55f'))
print(x)
print(regAns)
print(format(x-ans**2, '55f'))

