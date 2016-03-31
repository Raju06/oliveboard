alist=[]
inp='0'
while inp!=['1']:
	inp=raw_input().split(' ')
	alist.append(inp)
	print inp

alist=alist[:len(alist)-1]
print alist



