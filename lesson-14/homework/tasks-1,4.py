import numpy as np
#task1
@np.vectorize
def f_to_c(f):
    return (f-32)*5/9
f_temps = np.array([32,68,100,212,77])
c_tamps = f_to_c(f_temps)
print(c_tamps)

#task4
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

solution = np.linalg.solve(A, B)

print(solution)
