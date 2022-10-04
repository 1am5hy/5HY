import numpy as np

a = np.array([[2, 2], [1, 1]])
b = np.array([[2, 2], [1, 1]])
c = np.multiply(a, b)
print(c)

d = np.matmul(b, a)
e = c + d
print(d)

f = e + d
print(f)
