#!/usr/bin/python3
"""
    Program:        tempdiff.py
    Author:         Peter Southwick
    Date:           06/28/16
    Description:    A Short program that uses provided temperature data over a time period and
                    calculates the first, second differences, and tries to find the best calculated
                    curve it can create to mimic the provided data.

"""
import numpy as np


def factors(marray):  # Compute factors in marray
    n = marray.size
    mf = np.zeros(n-1)  # array of factors
    for j in range(n-1):
        mf[j] = marray[j+1]/marray[j]
    return mf

temp = np.array([51, 56, 60, 65, 73, 78, 85, 86, 84, 81, 80, 70])

tempFactors = factors(temp)  # Calculate the factors from the given temp data
firstDiff = np.diff(temp)  # Calculate the first difference
secondDiff = np.diff(firstDiff)  # Calculate the second difference
tempMean = np.mean(tempFactors)  # Calculate the mean of the factors

calculatedTemps = np.zeros(temp.size)
calculatedTemps[0] = temp[0]
for i in range(temp.size - 1):  # Calculate our estimated temp totals using the factor mean
    calculatedTemps[i+1] = tempMean * calculatedTemps[i]

xi = 0.0
xf = 12.0
sn = np.size(temp)
x = np.linspace(xi, xf, sn)
deg = 4  # Degree of our desired polynomial
poly = np.polyfit(x, temp, deg)
xc = np.linspace(xi, xf, 30)  # new x points
yc = np.polyval(poly, xc)  # new y points


print("Original list:", temp)
print("First diff:", firstDiff)
print("Second diff:", secondDiff)
print("Factors:", tempFactors)
print("Mean:", tempMean)
print("Calculated Temps using the mean of factors: ", calculatedTemps)
print("Our PolyFit Coefficients:", poly)
print("Evaluation of our curve fitted polynomial")
for j in range(30):
    print(xc[j], yc[j])