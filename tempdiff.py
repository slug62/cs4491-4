#!/usr/bin/python3

import numpy as np

temp = np.array([51, 56, 60, 65, 73, 78, 85, 86, 84, 81, 80, 70])

firstDiff = np.diff(temp)
secondDiff = np.diff(firstDiff)

print(firstDiff)
print(secondDiff)
