fh=open("samplewords.txt", "r")

for line in fh:
	samplewords=line.split()
print samplewords[len(samplewords)-1]
for i in range(len(samplewords)):
	if len(str(samplewords[i]))>7:
		samplewords.remove(samplewords[i])
	

#print samplewords
#print len(samplewords)
fh.close()
