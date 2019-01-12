from math import *
def polysum(n,s):
    """ Takes two arguments:
        n and s

        n for number of sides

        s for length of a side (as a regular polygon)

        returns sum of area of regular polygon and square of its perimeter
        rounded to 4 decimal places
    """
    return round(((0.25*n*s*s)/(tan(pi/n)) + (n*s)**2), 4)