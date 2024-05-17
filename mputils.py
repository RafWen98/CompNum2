import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpmath import mp


#Taylor expansion as defined by angabe
def sinTaylor(x, n, prec):
    """Taylor expansion of sin(x) with n terms"""
    mp.dps = prec
    sum = 0
    for i in range(n):
        #print(i)
        sum += mp.power(-1, i) * mp.power(x, (2 * i + 1)) / mp.fac(2 * i + 1)
    return sum

#Taylor expansion as defined by angabe
def sinTaylorReversed(x, n, prec = 15):
    """Taylor expansion of sin(x) with n terms"""
    mp.dps = prec
    sum = 0
    for i in range(n):
        j = n-i-1
        #print(j)
        sum += mp.power(-1, j) * mp.power(x, (2 * j + 1)) / mp.fac(2 * j + 1)
    return sum