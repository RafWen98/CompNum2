import numpy as np
import matplotlib.pyplot as plt

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
    return np.abs(f(x) - P(x))

# Define the interval and the number of nodes
a, b = 0, np.pi
n = 10  # You can change this for different number of nodes

# Equidistant nodes
xi_equi = equidistant_nodes(a, b, n)
yi_equi = f(xi_equi)

# Chebyshev nodes
xi_cheby = chebyshev_nodes(a, b, n)
yi_cheby = f(xi_cheby)

# Dense grid for plotting and error analysis
x_dense = np.linspace(a, b, 1000)
y_true = f(x_dense)

# Interpolation at equidistant nodes
P_equi = lagrange_interpolation(x_dense, xi_equi, yi_equi)

# Interpolation at Chebyshev nodes
P_cheby = lagrange_interpolation(x_dense, xi_cheby, yi_cheby)

# Compute errors
errors_equi = compute_errors(f, lambda x: lagrange_interpolation(x, xi_equi, yi_equi), x_dense)
errors_cheby = compute_errors(f, lambda x: lagrange_interpolation(x, xi_cheby, yi_cheby), x_dense)

# Plotting the results
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(x_dense, y_true, label='True function', color='black')
plt.plot(x_dense, P_equi, label='Equidistant nodes', linestyle='dashed')
plt.plot(x_dense, P_cheby, label='Chebyshev nodes', linestyle='dotted')
plt.scatter(xi_equi, yi_equi, color='blue', marker='o', label='Equidistant nodes')
plt.scatter(xi_cheby, yi_cheby, color='red', marker='x', label='Chebyshev nodes')
plt.legend()
plt.title('Interpolation Comparison')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 2, 2)
plt.plot(x_dense, errors_equi, label='Error: Equidistant nodes', linestyle='dashed')
plt.plot(x_dense, errors_cheby, label='Error: Chebyshev nodes', linestyle='dotted')
plt.yscale('log')
plt.legend()
plt.title('Error Comparison (Log Scale)')
plt.xlabel('x')
plt.ylabel('Error')

plt.tight_layout()
plt.show()

# Print maximum errors
max_error_equi = np.max(errors_equi)
max_error_cheby = np.max(errors_cheby)

print(f'Maximum error (Equidistant nodes): {max_error_equi}')
print(f'Maximum error (Chebyshev nodes): {max_error_cheby}')