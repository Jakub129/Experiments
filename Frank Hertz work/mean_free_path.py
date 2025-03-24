# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:53:05 2025

@author: jm3554
"""
# equation (4) and (5) in the script
def pressure(T):
    return 8.7*10**(9-(3110/T))

def mfp(T):
    k = 1.38*10**-23
    p = pressure(T)
    sigma = 2.1*10**-19
    return ((k*T) / (p*sigma))


# list of temperatures from 140-->200 in steps of 1
temps = [x for x in range(140,200,1)]

# use the equations above for y-values for each temp
mean_free_path = [mfp(x+273) for x in temps]
pressure_test = [pressure(x+273) for x in temps]

import matplotlib.pyplot as plt

# plot the mean-free-path against temp
plt.plot(temps, mean_free_path, ls="none", marker="o")

# pressure plot
# plt.plot(temps, pressure_test, ls="none", marker="o")