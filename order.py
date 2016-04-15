def sortwords(a1,a2):
	x=min(len(a1),len(a2))
	ret=0
	for i in range(x):
		if ord(a1[i])>ord(a2[i]):
			ret=1
			break
		else:
			if ord(a1[i])<ord(a2[i]):
				ret=2
				break
	
	if ret==0:
		if len(a1)>=len(a2):
			ret= 1
		else:
			ret =2

	if ret==1:
		return 1
	else:
		return 0

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
        		        	
            if sortwords(alist[i],alist[i+1])==1:
            	
            	temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            
alist=raw_input().split()

bubbleSort(alist)
print " ".join(alist)
	