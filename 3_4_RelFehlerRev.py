import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol


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
    savefig= 'figs/3_4.png'
    accuracy = 100*10e-16
    k_max = 8

    #x_values = [2 ** k for k in range(k_max + 1)]
    x_values = [2 ** k for k in range(k_max + 1)] + [710]

    n_values, VF = utils.n_needed_for_accuracy(x_values, accuracy)
    Rel_errors = np.array(calculate_errors_nat_rev(x_values, n_values, order = 'nat'))
    Rel_errors_rev = np.array(calculate_errors_nat_rev(x_values, n_values, order = 'rev'))

    diff = Rel_errors - Rel_errors_rev

    headers =['x', 'n', 'Rel_error_natuerlich', 'Rel_error_reversed', 'diff']
    int_cols = ['x', 'n']
    utils.plot_table(x_values, n_values, Rel_errors, Rel_errors_rev, diff, headers=headers, int_columns=int_cols, savefig=savefig)