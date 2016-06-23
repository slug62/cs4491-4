#!/usr/bin/python3

import numpy as np

patients = np.array([5500, 8500, 13500, 20500, 29500, 40500, 53500, 68500])

firstDiff = np.diff(patients)
secondDiff = np.diff(firstDiff)

print(firstDiff)
print(secondDiff)
