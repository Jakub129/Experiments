# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
%matplotlib inline
%config InlineBackend.figure_format='retina'


# Function to read data from a text file
def read_data_from_file(file_path):
    # Assuming the file has two columns, and space/tab separated
    data = np.loadtxt(file_path)
    return data[:, 0], data[:, 1]  # Return the two columns separately


x_data , y_data = read_data_from_file("Data140.txt")

#plt.plot(x_data, y_data, ls="none", marker=".", markersize=2 )


coefficients = np.polyfit(x_data, y_data, 600)
p = np.poly1d(coefficients)
y_data = p(x_data)


#plt.plot(x_data, y_data , ls="none", marker=".", markersize=2 )
inverted_y_data = -y_data


minima_indices, _ = find_peaks(inverted_y_data)
plt.grid()

a = x_data[minima_indices]
b = sorted([x for x in set(a)])[3:-6]



xdat = [x for x in range(0,len(b))]
plt.plot(xdat, b, ls="none", marker="o")
plt.plot()

from scipy.optimize import curve_fit

def func(x, m, c):
    y = m*x+c
    return y


popt, pcov = curve_fit(func, xdat, b)
slope, intercept = popt
ydat = [func(x, slope, intercept) for x in xdat]


plt.plot(xdat, ydat)
print(f"slope: {slope}\n intercept: {intercept}\n\n\n")




# Output the indices and the corresponding x and y values of the minima
#print("Indices of minima:", minima_indices)
print("x values at the minima:", b)
#print("y values at the minima:", y_data[minima_indices])