import numpy as np
@np.vectorize
def f_to_c(f):
    return (f-32)*5/9
f_temps = np.array([32,68,100,212,77])
c_tamps = f_to_c(f_temps)
print(c_tamps)
