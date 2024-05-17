import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import qol

def arg_redukt(x, result_multi = 1):

    #checkif x is not in [0,2pi]
    if 2*np.pi <= x:
        #calc modulo and reasign x
        #k = x % (2 * np.pi)
        k = int(x/(2*np.pi))
        print(k)
        r = x - 2*k*np.pi
        x=r
    elif x < 0:
        arg_redukt(-x, -1)

    #check if in [0,1pi] or [pi,2pi]
    if x < np.pi:
        x = x
    elif np.pi <= x:
        #something
        x = x - np.pi
        result_multi = result_multi * -1
    else:
        print("something fugged up")

    return x , result_multi

if __name__ == "__main__":
    x_vals = [ 2, 4, -7, 16, 2*np.pi, 3*np.pi, 10]

    for x in x_vals:
        x_red, result_multi = arg_redukt(x)

        n, VF = utils.n_needed_for_accuracy(x_red)
        res = result_multi * utils.sinTaylorReversed(x_red,n)
        exact = math.sin(x)
        print (x, ": ", res/exact)
        print (res, " --- ", exact)

