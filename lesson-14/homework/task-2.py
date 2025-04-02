import numpy as np

def powerr(n,p):
    return n**p
vectorized_power = np.vectorize(powerr)
n = np.array([2, 3, 4, 5])
p = np.array([1, 2, 3, 4])
result = vectorized_power(n,p)
print(result)