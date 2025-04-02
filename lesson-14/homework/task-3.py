import numpy as np
a = np.array([
    [4,5,6],
    [3,-1,1],
    [2,1,-2]
])
b = np.array([7,4,5])
result = np.linalg.solve(a,b)
print(result)