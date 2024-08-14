import numpy as np

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])

print(X + Y)
print("////")
print(2 * Y)
print("////")
print(X * Y)
print("////")
print(np.dot(X, Y))
print("////")
print(np.sin(X))
print("////")
print(X.T)
