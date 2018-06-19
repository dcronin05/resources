def mult_iter(a, b):
    result = 0
    print('b is', b)
    while b > 0:
        result += a
        print('result is', result)
        b -= 1
        print('b is', b)
    return result

print(mult_iter(4, 4))


def mult(a, b):
    if b == 1:
        return a
    else:
        return a * mult(a, b-1)

a = 16
b = 16

print(a, '*', b, 'is', mult(a, b))


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(fact(4))


def iterpower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base*iterpower(base, exp-1)


print('iterpower(4, 0) =', iterpower(4, 2))


def iter_power(base, exp):
    '''
    :param base:
    :param exp:
    :return:
    '''

    if exp == 0:
        return 1
    result = base
    iter_var = exp
    for i in range(exp-1):
        # print(result, '*', base, '=', result * base)
        result = result * base


print(iter_power(2.52, 0))


def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)


moves = 0


class Recursion:

    moves = 0

    def printmove(self):
        self.moves += 1

    def towers(self, n, fr, to, spare):
        print(moves)
        if n == 1:
            self.printmove()
        else:
            self.towers(n-1, fr, spare, to)
            self.towers(1, fr, to, spare)
            self.towers(n-1, spare, to, fr)


test = Recursion()

test.towers(8, 'P1', 'P2', 'P3')
print(test.moves)
