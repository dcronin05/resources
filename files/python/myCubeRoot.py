x = 'start'

while int != type(x):
    try:
        x = int(input('Enter a number: '))
    except:
        print('That was not a number!')
        continue

ans = 0

while ans**3 < x:
    ans = ans + 0.0000001
    # print(ans)
if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube')
    print('Exited with ', ans)
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
