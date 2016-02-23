import numpy as np
import itertools
 
list1=['A','B','C','D','E','F','G','H']
list2=['history','chemistry','english','biology','hindi','physics','geography','math']
arr = np.empty((len(list1),len(list2)), dtype=object)

iterables=['A','B','C','D','E','F','G','H']
iterables2=['history','chemistry','english','biology','hindi','physics','geography','math']
for t in itertools.permutations(iterables,8):
	for k in itertools.permutations(iterables2,8):
		a=[]
		for item in range(8):
			a.append(t[item])
			a.append(k[item])
		found=False
		l=0
		o=0	
		while not found:
			if (a[l]=='E' and a[l+1]=='hindi') and (a[o]=='C' and ((a[o+1]=='english') or (a[o+1]=='geography'))):	
				print a
				found=True
			if l==8:
				
			l+=1
			o+=1