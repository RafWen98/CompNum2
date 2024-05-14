import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol

picklefile = "data.pickle"
data = qol.load_data(picklefile)

eps = 10e-16                                #machine accuracy (it think)               
accuracy = 100 * eps
n_x = 10                                    #number of x samples where the function will be plotted
spacing = np.linspace(0, 0.5*np.pi, n_x)          #Definitionsbereich

#reset dict for new data
data["3_2"] = {}

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

    #populate dict with data to save in picklefile
    data["3_2"][i] = {
        'x' : x,
        'n' : n,
        'VF' : VF,
    }

qol.save_data(picklefile, data)

#just testing
""" data = qol.load_data(picklefile)
print(data["3_2"][3]['VF'])
print(data["3_2"][3]['n'])
print(data["3_2"][3]['x']) """

    
