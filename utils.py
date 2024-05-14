import math
import numpy as np


#Taylor expansion as defined by angabe
def sinTaylor(x, n):
    """Taylor expansion of sin(x) with n terms"""
    sum = 0
    for i in range(n):
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)
    return sum

#Verfahrensfehler as establsihed in angabe 3.2
def Verfahrensfehler(x, n, set_cos=1):
    """Verfahrensfehler per cosinus abschaetzung"""
    sum = pow(-1, n+1) * pow(x, (2 * n + 3)) / math.factorial(2 * n + 3) * set_cos
    return sum

#Relativerfehler für 3.3
def Relativerfehler(x, n):
    """Relativfehler mit Bezugsgröße durch Standardprozedur"""
    tay = sinTaylor(x,n)
    sin = math.sin(x)
    rel = abs((tay-sin)/sin)
    return rel
