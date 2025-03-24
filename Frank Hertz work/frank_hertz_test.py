# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:00:05 2025

@author: jm3554
"""

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

def read_data_from_file(file_path):
    data = np.loadtxt(file_path)
    return data[:, 0], data[:, 1]


# read the text file
x_data , y_data = read_data_from_file("Data140.txt")

# cut off a section of the graph for close-up
testx = x_data[350:410]
testy = y_data[350:410]

plt.plot(testx, testy, ls="none", marker=".", markersize=2 )

# fit a polynomial to smooth the data
coefficients = np.polyfit(testx, testy, 3)
p = np.poly1d(coefficients)
testy = p(testx)

# plot the close-up
plt.plot(testx, testy)
inverted_y_data = -testy

minima_indices, _ = find_peaks(inverted_y_data)
plt.grid()

a = x_data[minima_indices]
b = set(a)
# Output the indices and the corresponding x and y values of the minima
#print("Indices of minima:", minima_indices)
print("x values at the minima:", b)
#print("y values at the minima:", y_data[minima_indices])