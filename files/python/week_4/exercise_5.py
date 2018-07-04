def foo(x, a):

    count = 0
    while x >= a:
        print('Entering while loop in foo()')
        count += 1
        print('count += 1')
        print(x, '=', x, '-', a)
        x = x - a
        print(x)

    return count


print(foo(234234, 5))