num=["1","2","3"]
alpha=["a","b","c"]
sym=["!","@","#"]
element=[]
newlist=[]
for i in num:

	for j in alpha:
		for k in sym:
			element.append(i)
			element.append(j)
			element.append(k)
			newlist.append(element)
			element=[]

print newlist
print len(newlist)
poppedlist=[]
for item in newlist:
	if ("2" in item and "c" in item):
		print "inside if"
		poppedlist.append(newlist.pop(newlist.index(item)))

print newlist
print len(newlist)

print poppedlist