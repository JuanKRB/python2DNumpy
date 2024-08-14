
import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

# Shows dimensions
print(A.ndim)

# returns a tuple corresponding to
# the size or number of each dimension.
print(A.shape)

print(A.size)

print("////")

# Two different ways
print(A[1, 2])
print(A[1][2])

print("////")

print(A[0][0:2])

print(A[0:2, 2])