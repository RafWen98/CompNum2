import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
        

n = 50              #number of terms for taylor expansion
n_x = 10            #number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5, n_x)          #Definitionsbereich

for x in spacing:
    ax = x * np.pi
    ysin = math.sin(ax)
    ytay = utils.sinTaylor(ax, n)
    print(ax)
    plt.plot(ax, ysin, 'rx', lw=1)  # Plot sin(x)
    plt.plot(ax, ytay, 'bo', lw=1)  # Plot Taylor approximation
    print(ysin, " : ", ytay)

plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend(['sin(x)', 'Taylor approximation'])
plt.show()

#plt.savefig(f'sin_approx_{x}.png')  # Save the plot as an image file
