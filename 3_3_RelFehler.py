import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol


def calculate_errors(x_values, n_values):
    errors = []

    for i, x in enumerate(x_values):
        n = n_values[i]
        approx_value = utils.sinTaylor(x, n)
        exact_value = math.sin(x)
        rel_error = abs(approx_value - exact_value) / abs(exact_value)

        errors.append(rel_error)

        print(f"x: {x}, n used: {n}, Relative Error: {rel_error}")

    return errors

if __name__ == "__main__":
    savefig= 'figs/3_3.png'
    accuracy = 100*10e-16
    k_max = 8

    x_values = [2 ** k for k in range(k_max + 1)] + [710]

    n_values, VF = utils.n_needed_for_accuracy(x_values, accuracy)
    Rel_errors = calculate_errors(x_values, n_values)
    print(len(x_values))
    print(n_values)
    print(len(Rel_errors))

    headers =['x', 'n', 'Rel_error_natuerlich']
    int_cols = ['x', 'n']
    utils.plot_table(x_values, n_values, Rel_errors, headers=headers, int_columns=int_cols, savefig=savefig)