import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol                          #random Quality of Life functions

picklefile = "data.pickle"
data = qol.load_data(picklefile)


ks = np.linspace(0, 7, 8)                    #k values from 0,1,2,3, 4,5,6,7
eps = 10e-16                                #machine accuracy (it think)               
accuracy = 100 * eps
n_x = 10                                    #number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5*np.pi, n_x)          #Definitionsbereich

print(ks)

for k in ks:

    x = 2 ** k 


    RF = utils.Relativerfehler(x, n)
    print(n, " number of terms needed for x =", x)
