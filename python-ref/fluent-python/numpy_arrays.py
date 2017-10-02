#!/usr/bin/env python3

"A brief example of NumPy from chapter 2."

import numpy

from demo import headline

print(headline("General"))
a = numpy.arange(12)
print("a:", a)
print("type(a):", type(a))
print("a.shape:", a.shape)
a.shape = 3, 4
print("a.shape:", a.shape)
print("a:", a)
print("a[2]:", a[2])
print("a[2, 1]:", a[2, 1])
print("a[:, 1]:", a[:, 1])

# transpose == swapping rows with columns
print("a.transpose():", a.transpose())
