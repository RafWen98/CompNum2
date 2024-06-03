import utils
import csv


if __name__ == "__main__":
    savefig= 'figs/kond.png'

    # File path to the CSV file
    file_path = 'kondition.csv'

    # Lists to store the data from each column
    x_values = []
    kond = []

    # Reading the CSV file
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            x_values.append(int(row[0]))
            kond.append(float(row[1]))

    # Print the columns
    print("Column 1:", x_values)
    print("Column 2:", kond)


    headers = ['x', 'Kondition']
    int_cols = ['x']

    utils.plot_table(x_values, kond, headers=headers, int_columns=int_cols, savefig=savefig, size = (6,4))

    