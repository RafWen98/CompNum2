import math
import numpy as np
import pickle
import os


# Load shot data from a file if it exists, otherwise return an empty dictionary
def load_data(filename):  
    """-- Load shot data from a file if it exists, otherwise return an empty dictionary --"""                                 
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:
        return {}
    
def save_data(filename, data):
    """-- Save shot data to a file called filename --"""                       
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        print("---data pickled---")


#verfahrensfehler entwicklung as defined by 3.2
def VerfahrensfehlerSin(x, n):
    """Taylor expansion of sin(x) with n terms"""
    sum = 0
    for i in range(n):
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)

    VF = math.sin(x)- sum      #defined by angabe (3.2)
    return VF

#float als bruch von pi darstellen, doesnt really work
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