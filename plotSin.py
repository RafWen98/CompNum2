import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us


n = 50              # Number of terms for Taylor expansion
n_x = 100           # Number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5, n_x) * np.pi          # Definitionsbereich

# Create arrays to store x and y values for sine function and its Taylor approximation
x_values = []
y_sin_values = []
y_taylor_values = []

for x in spacing:
    y_sin = math.sin(x)
    y_taylor = utils.sinTaylor(x, n)
    x_values.append(x)
    y_sin_values.append(y_sin)
    y_taylor_values.append(y_taylor)

plt.plot(x_values, y_sin_values, 'red', lw=1, label="sin(x)")  # Plot sin(x)
plt.plot(x_values, y_taylor_values, 'blue', lw=1, label="taylor")  # Plot Taylor approximation

plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend()
plt.show()