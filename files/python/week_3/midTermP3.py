def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    result = {}
    exp = 0
    answer = 1000
    count = 0

    for i in range(50):
        result[exp] = abs(base**exp - num)
        exp += 1

    for i in result:
        if result[i] > result[i+1]:
            continue
        else:
            return i


print(closest_power(2, 192.0))
