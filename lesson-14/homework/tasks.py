import numpy as np
#task1
@np.vectorize
def f_to_c(f):
    return (f-32)*5/9
f_temps = np.array([32,68,100,212,77])
c_tamps = f_to_c(f_temps)
print(c_tamps)

#task2
def power_function(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_function)

arr1 = np.array([2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4])

result = vectorized_power(arr1, arr2)

print(result)
#task3
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

solution = np.linalg.solve(A, B)

print(solution)
#task4
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

solution = np.linalg.solve(A, B)

print(solution)
