import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us

eps = 10e-16                                #machine accuracy (it think)               
accuracy = 100 * eps
n_x = 10                                    #number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5*np.pi, n_x)          #Definitionsbereich

for i, x in enumerate(spacing):
    #init/reset values for iterator and Verfahrensfehler
    VF = 100
    n = 0

    #loop as long as verfahrensfehler is bigger than accuracy
    while VF > accuracy:
        n=n+1
        VF = abs(utils.Verfahrensfehler(x, n, set_cos = 1))
        #print(VF)
    print(n, " number of terms needed for x =", x)




    
