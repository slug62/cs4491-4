#!/usr/bin/python3
"""
    Program:        patientdiff.py
    Author:         Peter Southwick
    Date:           06/28/16
    Description:    A Shorty program that uses provided patient data over a time period and
                    calculates the first, second differences
"""
import numpy as np

patients = np.array([5500, 8500, 13500, 20500, 29500, 40500, 53500, 68500])

firstDiff = np.diff(patients)
secondDiff = np.diff(firstDiff)

print("Original list:", patients)
print("First diff:", firstDiff)
print("Second diff:", secondDiff)
