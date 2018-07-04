def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """

    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)


def f(n):
    '''

    :param n: integer
    :return:
    '''

    if n == 0:
        return n+1
    else:
        return n * f(n-1)


# print(rem(2, 5))

print(f(3))