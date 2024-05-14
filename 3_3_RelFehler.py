import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol

def relative_error(approx, exact):
    return 

def n_needed_for_accuracy(x, accuracy = 100*10e-16):
    """calulates the needed n for a desired accuracy of sin(x)"""
    VF = 100; n = 0
    #loop as long as verfahrensfehler is bigger than accuracy
    while VF > accuracy:
        n=n+1
        VF = abs(utils.Verfahrensfehler(x, n, set_cos = 1))
    return n, VF

def calculate_errors():
    k_max = 10
    x_values = [2 ** k for k in range(k_max + 1)] + [710]
    reference_values = [math.sin(x) for x in x_values]

    for i, x in enumerate(x_values):
        n, VF = n_needed_for_accuracy(x)
        approx_value = utils.sinTaylor(x, n)  # Using n=10 as an example
        exact_value = reference_values[i]
        rel_error = abs(approx_value - exact_value) / abs(exact_value)
        print(f"Argument: {x}, n used: {n}, Relative Error: {rel_error}")

calculate_errors()