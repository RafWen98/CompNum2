import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol
from mpmath import mp

def f(x):
    return np.sin(x)  # Example function

def equidistant_nodes(a, b, n):
    return np.linspace(a, b, n)

def chebyshev_nodes(a, b, n):
    k = np.arange(1, n + 1)
    x = np.cos((2 * k - 1) * np.pi / (2 * n))
    return 0.5 * (b - a) * (x + 1) + a

def lagrange_basis(x, xi, j):
    basis = np.ones_like(x)
    for m in range(len(xi)):
        if m != j:
            basis *= (x - xi[m]) / (xi[j] - xi[m])
    return basis

def lagrange_interpolation(x, xi, yi):
    L = np.zeros_like(x)
    for j in range(len(xi)):
        L += yi[j] * lagrange_basis(x, xi, j)
    return L

def compute_errors(f, P, x):
    return np.abs((f(x) - P(x)))
    #return np.abs((f(x) - P(x))/f(x))



if __name__ == "__main__":
    savefig= 'figs/3_7.png'
    accuracy = 100*10e-16
    mp.dps = 25

    # Define the interval and the number of nodes
    a, b = 0, np.pi
    n_nodes = 20 # You can change this for different number of nodes

    # Dense grid for plotting and error analysis
    x_dense = np.linspace(a, b, 1000)
    y_true = np.sin(x_dense)

    # Taylor
    xi_tay = np.linspace(a, b, n_nodes)
    n_tay_max = np.max(utils.n_needed_for_accuracy(xi_tay))
    yi_tay = utils.sinTaylorReversed(xi_tay, n_tay_max)

    #n_nodes = int(n_tay_max)
    
    # Equidistant nodes
    xi_equi = equidistant_nodes(a, b, n_nodes)
    yi_equi = f(xi_equi)

    # Chebyshev nodes
    xi_cheby = chebyshev_nodes(a, b, n_nodes)
    yi_cheby = f(xi_cheby)

    # Interpolation at equidistant nodes
    P_equi = lagrange_interpolation(x_dense, xi_equi, yi_equi)

    # Interpolation at Chebyshev nodes
    P_cheby = lagrange_interpolation(x_dense, xi_cheby, yi_cheby)

    P_tay = utils.sinTaylorReversed(x_dense, n_tay_max)

    # Compute errors
    errors_equi = compute_errors(f, lambda x: lagrange_interpolation(x, xi_equi, yi_equi), x_dense)
    errors_cheby = compute_errors(f, lambda x: lagrange_interpolation(x, xi_cheby, yi_cheby), x_dense)
    errors_tay = compute_errors(f, lambda x: utils.sinTaylorReversed(x, n_tay_max), x_dense)

    #exact_value = f(xi_tay)
    #print(exact_value, " --- ", mp_value )
    #errors_tay = abs((yi_tay - exact_value) / exact_value)



    # Plotting the results
    plt.figure(figsize=(14, 7))

    plt.subplot(1, 2, 1)
    plt.plot(x_dense, y_true, label='True function', color='black')
    #plt.plot(x_dense, P_equi, label='Equidistant nodes', linestyle='dashed')
    #plt.plot(x_dense, P_cheby, label='Chebyshev nodes', linestyle='dotted')
    #plt.plot(x_dense, P_tay, label='Sin Taylor Reversed', linestyle=':')
    plt.scatter(xi_tay, yi_tay, color='g', marker='s', label='Sin Taylor Reversed')
    plt.scatter(xi_equi, yi_equi, color='blue', marker='o', label='Equidistant nodes')
    plt.scatter(xi_cheby, yi_cheby, color='orange', marker='x', label='Chebyshev nodes')
    plt.legend()
    plt.title(f'Interpolation Comparison with {n_nodes} n_nodes')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.subplot(1, 2, 2)
    plt.plot(x_dense, errors_tay, label='Error: Sin Taylor Reversed', linestyle='dotted', c='g')
    plt.plot(x_dense, errors_equi, label='Error: Equidistant nodes', linestyle='dotted', c='b')
    plt.plot(x_dense, errors_cheby, label='Error: Chebyshev nodes', linestyle='dotted', c='orange')
    plt.yscale('log')
    plt.legend()
    plt.title('Error Comparison (Log Scale)')
    plt.xlabel('x')
    plt.ylabel('Error')

    plt.tight_layout()
    plt.savefig(savefig)
    plt.show()

    # Print maximum errors
    max_error_equi = np.max(errors_equi)
    max_error_cheby = np.max(errors_cheby)
    max_error_tay = np.max(errors_cheby)

    print(f'Maximum error (Equidistant nodes): {max_error_equi}')
    print(f'Maximum error (Chebyshev nodes): {max_error_cheby}')
    print(f'Maximum error (sin Taylor Reversed): {max_error_tay}')