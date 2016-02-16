alist=map(int,raw_input().split())
from numpy import inv
a=np.array([[1,1,1],[4,2,1],[9,3,1],[16,4,1]])
ainv = inv(a)
print ainv