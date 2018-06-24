from math import *

def polysum(n, s):
    '''
    Takes the number of sides of a polygon and the number of sides and returns the sum of the area and square of the perimiter.
    :param n: int or float
    :param s: int or float
    :return: float rounded to 4 decimal places
    '''

    area = (0.25*n*s**2) / tan(pi/n)

    perimeter = s * n

    return round((perimeter**2 + area), 4)
