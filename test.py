import math
import numpy as np
import matplotlib.pyplot as plt


def sinTaylor (x, n):
    """Taylor expansion of sin(x) with n terms"""
    i = 0
    sum = 0
    while i < n:
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / (math.factorial(2 * i + 1))
        i = i + 1
    return sum
        

n = 50              #number of terms for taylor expansion
n_x = 10            #number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5, n_x)          #Definitionsbereich

for x in spacing:
    ax = x * np.pi
    ysin = math.sin(ax)
    ytay = sinTaylor(ax, n)
    print(ax)
    plt.plot(ax, ysin, 'r')  # Plot sin(x)
    plt.plot(ax, ytay, 'b')  # Plot Taylor approximation
    print(ysin, " : ", ytay)

plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend(['sin(x)', 'Taylor approximation'])

plt.savefig(f'sin_approx_{x}.png')  # Save the plot as an image file
plt.show()