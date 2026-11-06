import numpy as np

def make_arrays(size,low,high):
    a = np.random.randint(low, high+1, size)
    b = np.random.randint(low, high+1, size)
    return a, b, a * b, a.sum(), b.sum()

print(make_arrays((2, 3), 1, 100))