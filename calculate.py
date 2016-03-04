import numpy as np
ind_set_count2=np.array([4,5,6])
ind_set_count3=np.array([2,3,4])
ind_set=[]
k=list(np.random.choice(ind_set_count2,2))
print k
print k[0]
for i in k:
	ind_set.append(i)

print ind_set