import math
import numpy as np


def sinTaylor(x, n):
    """Taylor expansion of sin(x) with n terms"""
    sum = 0
    for i in range(n):
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)
    return sum

def VerfahrensfehlerSin(x, n):
    """Taylor expansion of sin(x) with n terms"""
    sum = 0
    for i in range(n):
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)

    VF = math.sin(x)- sum      #defined by angabe (3.2)
    return VF

def Verfahrensfehler(x, n, set_cos=1):
    """Verfahrensfehler per cosinus abschaetzung"""
    sum = pow(-1, n+1) * pow(x, (2 * n + 3)) / math.factorial(2 * n + 3) * set_cos
    return sum


def fraction_of_pi(x):
    # Calculate the fraction of pi
    numerator = int(x * 2)
    denominator = 2
    
    # Simplify the fraction by finding the greatest common divisor
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    # If the denominator is 1, return only the numerator
    if denominator == 1:
        return f"{numerator}π"
    else:
        return f"{numerator}π/{denominator}"