import numpy as np
a = np.array([[1,1,1,1],[8,4,2,1],[27,9,3,1],[64,16,4,1]])
b = np.array([0,6,24,60])
x = np.linalg.solve(a, b)
print (x[0]*125)+(x[1]*25)+(x[2]*5)+(x[3]*1)