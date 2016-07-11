#!/usr/bin/python3
"""
    Program:        patientcurve.py
    Author:         Peter Southwick
    Date:           07/11/16
    Description:    A Short program that takes provided patient data, creates a polynomial from it and then
                    evaluates the polynomial for intermediate values.

"""
import numpy as np
import matplotlib.pyplot as plot
from tabulate import tabulate


def factors(marray):  # Compute factors in marray
    n = marray.size
    mf = np.zeros(n-1)  # array of factors
    for j in range(n-1):
        mf[j] = marray[j+1]/marray[j]
    return mf

providedpatientdata = np.array([5500, 8500, 13500, 20500, 29500, 40500, 53500, 68500])
provideddatayears = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002]

# Compute a polynomial from the provided data
xi = 0.0  # Initial value of X
xf = 8.0  # Final value of X
sn = np.size(providedpatientdata)  # How many values of X we want
x = np.linspace(xi, xf, sn)  # Creating an evenly distributed number of X's between xi, xf
deg = 3  # Degree of our desired polynomial
poly = np.polyfit(x, providedpatientdata, deg)  # Computing the polynomial from given data
xc = np.linspace(xi, xf, 30)  # Creating an evenly distributed number of X's for our computed polynomial
yc = np.polyval(poly, xc)  # Evaluate our computed polynomial

# Plot the graphs of both provided data, and computed data
f, linearr = plot.subplots(2, sharex=True)
linearr[0].set_title('Provided data')
linearr[0].plot(x, providedpatientdata, marker='o', linestyle='-')
linearr[1].set_title('Computed data')
linearr[1].plot(xc, yc, marker='o', linestyle='-')
plot.show()

# Create an easy to read table from data of evaluated polynomial
tableheaders = ['Computed X', 'Computed Y']
data = []
for i in range(len(xc)):
    data.append([xc[i], yc[i]])

# Output
print("Original list:", providedpatientdata)
print("Our PolyFit Coefficients:", poly)
print("Computing intermediate values by evaluating our computed polynomial")
print(tabulate(data, headers=tableheaders, tablefmt='fancy_grid', floatfmt='.4f'))