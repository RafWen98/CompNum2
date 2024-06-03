import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol
from mpmath import mp


def calculate_errors_nat_rev(x_values, n_values, order = 'nat'):
    errors = []

    for i, x in enumerate(x_values):
        n = n_values[i]
        #check which summation order to take
        if order == 'nat':
            approx_value = utils.sinTaylor(x, n)
        elif order == 'rev':
            approx_value = utils.sinTaylorReversed(x, n)
        else:
            print("sin aprrox function not found, exiting routine")
            exit(1)

        exact_value = math.sin(x)
        rel_error = abs(approx_value - exact_value) / abs(exact_value)

        errors.append(rel_error)
        #print(f"x: {x}, n used: {n}, Relative Error: {rel_error}")

    return errors

if __name__ == "__main__":
    savefig= 'figs/3_6.png'
    accuracy = 100*10e-16
    k_max = 8

    precision = 25
    mp.dps = precision

    x_values = [2 ** k for k in range(k_max + 1)] + [710]
    n_values, VF = utils.n_needed_for_accuracy(x_values, accuracy)

    red_rel_error = []

    for i, x in enumerate(x_values):
        n = n_values[i]
        x_red, res_multi = utils.arg_redukt(x, prec=precision)
        approx_value = res_multi*utils.sinTaylorReversed(x_red, n)

        #exact_value = math.sin(x)
        exact_value = mp.sin(x)
        #print(exact_value, " --- ", mp_value )
        rel_error = abs((approx_value - exact_value) / exact_value)

        red_rel_error.append(rel_error)

    red_rel_error = np.array(red_rel_error)

    Rel_errors = np.array(calculate_errors_nat_rev(x_values, n_values, order = 'nat'))
    Rel_errors_rev = np.array(calculate_errors_nat_rev(x_values, n_values, order = 'rev'))

    #calc diff of reversed summation and reduced reversed summation
    diff_rev = Rel_errors_rev - red_rel_error

    headers = ['x', 'n', 'Rel_error_natuerlich', 'Rel_error_reversed', 'Rel_error_reduced', 'diff']
    int_cols = ['x', 'n']
    utils.plot_table(x_values, n_values, Rel_errors, Rel_errors_rev, red_rel_error, diff_rev, headers=headers, int_columns=int_cols, savefig=savefig, size = (14,6))