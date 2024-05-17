import math                         #for math functions like sin and stuff
import numpy as np                  #for everything numericals 
import pandas as pd
import matplotlib.pyplot as plt     #for plots
import utils                        #utils.py file containg functions defined by us
import matplotlib.transforms


def plot_graph_and_table(*args, headers):
    """
    Plots a graph using the values from the input lists or numpy arrays with specified headers
    and places a table to the side of the graph.
    
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
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot the graph
    x_values = args[0]
    for array, header in zip(args[1:], headers[1:]):
        axs[0].plot(x_values, array, label=header, marker='x', linestyle='None', c='b')
        axs[0].plot(x_values, array, linestyle='dashed', c='b', alpha=0.5)
    
    axs[0].set_title('Glieder per x für gewünschte Genauigkeit')
    axs[0].set_xlabel(headers[0])
    axs[0].set_ylabel('n')
    axs[0].legend()
    axs[0].grid(True)
    
    # Plot the table
    axs[1].axis('tight')
    axs[1].axis('off')
    table = axs[1].table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.auto_set_column_width(col=list(range(len(df.columns))))
    table.scale(xscale=1, yscale=1)

    # Set the header text to be bold
    for key, cell in table.get_celld().items():
        if key[0] == 0:  # This is the header row
            cell.set_text_props(fontweight='bold')

    # Adjust layout to bring the table closer to the graph
    plt.subplots_adjust(wspace=-0.35)  # Adjust horizontal space between subplots
    plt.savefig('figs/3_2.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    eps = 10e-16                                #machine accuracy (it think)               
    accuracy = 100 * eps
    n_x = 10                                    #number of x samples where the function will be plotted
    spacing = np.linspace(0, 0.5*np.pi, n_x)          #Definitionsbereich
    k_max = 8
    x_values = [2 ** k for k in range(k_max + 1)] + [710]
    n_values = []

    for i, x in enumerate(x_values):
        #init/reset values for iterator and Verfahrensfehler
        VF = 100
        n = 0

        #loop as long as verfahrensfehler is bigger than accuracy
        while VF > accuracy:
            n=n+1
            VF = abs(utils.Verfahrensfehler(x, n, set_cos = 1))
            #print(VF)
        n_values.append(n)
        print(n, " number of terms needed for x =", x)

    plot_graph_and_table( x_values, n_values, headers=['x', 'n'])




    
