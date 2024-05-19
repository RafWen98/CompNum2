import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpmath import mp


#Taylor expansion as defined by angabe
def sinTaylor(x, n):
    """Taylor expansion of sin(x) with n terms"""
    sum = 0
    for i in range(n):
        #print(i)
        sum += pow(-1, i) * pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)
    return sum

#Taylor expansion as defined by angabe
def sinTaylorReversed(x_values, n_values):
    """Taylor expansion of sin(x) with n terms"""

    #so it can accept singel x input as well as an array of x_values as input
    if isinstance(x_values, (float, int)):
        x_values = [x_values]
        n_values = [n_values]
    
    sum = []
    for k, x in enumerate(x_values):
        if x == 0 or x==np.pi or x==2*np.pi:
            res = 0
        else:
            n = n_values[k]
            res = 0
            for i in range(n):
                j = n-i-1
                #print(j)
                res += pow(-1, j) * pow(x, (2 * j + 1)) / math.factorial(2 * j + 1)
        sum.append(res)

    if len(x_values) == 1:
        return sum[0]       #return single float when only single x was inputed
    else:
        return sum          

#Verfahrensfehler as establsihed in angabe 3.2
def Verfahrensfehler_raw(x, n, set_cos=1):
    """Verfahrensfehler per cosinus abschaetzung"""
    sum = pow(-1, n+1) * pow(x, (2 * n + 3)) / math.factorial(2 * n + 3) * set_cos
    sum = sum / math.sin(x)
    return sum

#Verfahrensfehler as establsihed in angabe 3.2 with conditions for x = 0, x=pi, x = 2pi
def Verfahrensfehler(x, n, set_cos=1):
    """Verfahrensfehler per cosinus abschaetzung"""
    if x == 0:
        sum = 0
    elif x == np.pi:
        sum = 0
    elif x == 2*np.pi:
        sum = 0
    else:
        sum = pow(-1, n+1) * pow(x, (2 * n + 3)) / math.factorial(2 * n + 3) * set_cos
        sum = sum / math.sin(x)
    return sum

#Relativerfehler für 3.3
def Relativerfehler(x, n):
    """Relativfehler mit Bezugsgröße durch Standardprozedur"""
    tay = sinTaylor(x,n)
    sin = math.sin(x)
    rel = abs((tay-sin)/sin)
    return rel

#
def n_needed_for_accuracy(x_values, accuracy = 100*10e-16):
    """calulates the needed n for a desired accuracy of sin(x)"""
    # Ensure x_values is a list
    if isinstance(x_values, (float, int)):
        x_values = [x_values]

    n_values = []
    VF_values = []
    for x in x_values:
        if x % np.pi == 0:
            n_values.append(1)
            VF_values.append(0)
        else:
            VF = 100
            n = 0
            # Loop as long as verfahrensfehler is bigger than accuracy
            while VF > accuracy:
                n += 1
                VF = abs(Verfahrensfehler(x, n, set_cos=1))  # Assuming Verfahrensfehler is defined elsewhere
            n_values.append(n)
            VF_values.append(VF)

    if len(x_values) == 1:
        return n_values[0], VF_values[0]
    else:
        return n_values, VF_values

#Arg reduction code for 3.5
def arg_redukt(x, result_multi = 1):

    #check if x is not in [0,2pi]
    if 2*np.pi <= x:
        #calc modulo and reasign x
        #k = x % (2 * np.pi)
        k = int(x/(2*np.pi))
        #print(k)
        r = x - 2*k*np.pi
        x=r
    elif x < 0:
        #swap signs of x and result_multi bc sin(x) = -sin(-x)
        return arg_redukt(-x, -1)

    #check if in [0,1pi] or [pi,2pi]
    if x < np.pi:
        x = x
    elif np.pi <= x:
        #project onto [0,1pi] and reverse result_multi 
        x = x - np.pi
        result_multi = result_multi * -1
    else:
        print("something didnt work out")
    #sin(x) = result_multi * sinTaylor(x,n)
    return x , result_multi 



def plot_graph_and_table(*args, headers):
    """
    Plots a graph using the values from the input lists or numpy arrays with specified headers
    and places a table below the graph.
    
    Parameters:
    *args : list or numpy array
        Variable number of lists or numpy arrays containing the values for each column.
    headers : list of str
        List of strings representing the headers for the table columns.
    """
    
    if len(headers) != len(args):
        raise ValueError("The number of headers must match the number of lists/arrays provided.")
    
    # Convert input to pandas DataFrame
    data = {header: array for header, array in zip(headers, args)}
    df = pd.DataFrame(data)
    
    # Create a figure with two subplots: one for the graph and one for the table
    fig, axs = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [2, 1]})
    
    # Plot the graph
    x_values = args[0]
    for array, header in zip(args[1:], headers[1:]):
        axs[0].plot(x_values, array, label=header, marker = 'x', linestyle = 'dashed')
    
    axs[0].set_xlabel(headers[0])
    axs[0].set_ylabel('Values')
    axs[0].legend()
    axs[0].grid(True)
    
    # Plot the table
    axs[1].axis('tight')
    axs[1].axis('off')
    table = axs[1].table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

    # Adjust layout to bring the table closer to the graph
    plt.subplots_adjust(hspace=0.05)  # Reduce the vertical space between the subplots
    plt.savefig('figs/3_2.png')
    plt.show()

def plot_table(*args, headers, int_columns=None, savefig = 'figs/unnamed.png', size = (9,4)):
    """
    Plots a table using the values from the input lists or numpy arrays with specified headers.
    
    Parameters:
    headers : list of str
        List of strings representing the headers for the table columns.
    *args : list or numpy array
        Variable number of lists or numpy arrays containing the values for each column.
    """
    
    if len(headers) != len(args):
        raise ValueError("The number of headers must match the number of lists/arrays provided.")
    
    # Convert input to pandas DataFrame
    data = {header: array for header, array in zip(headers, args)}
    df = pd.DataFrame(data)

    # Format specified columns to display integer values
    if int_columns is not None:
        for col in int_columns:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: f"{int(x)}" if pd.notnull(x) else "")
    
    # Plot the table
    fig, ax = plt.subplots(figsize=size)
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.auto_set_column_width(col=list(range(len(df.columns))))
    table.scale(xscale=1, yscale=2)

    # Set the header text to be bold
    for key, cell in table.get_celld().items():
        if key[0] == 0:  # This is the header row
            cell.set_text_props(fontweight='bold')
    
    """ # Adjust column widths
    cell_dict = table.get_celld()
    for col_idx in range(len(headers)):
        max_len = max([len(str(cell_dict[(row_idx, col_idx)].get_text().get_text())) for row_idx in range(len(df))] + [len(headers[col_idx])])
        for row_idx in range(len(df) + 1):
            cell_dict[(row_idx, col_idx)].set_width(0.3 * max_len) """
    
    plt.savefig(savefig, bbox_inches='tight')
    plt.show()
