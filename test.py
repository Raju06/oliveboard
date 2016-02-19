a=[i for i in range(10,100)]
print a
k=list(str(a[47]))[::-1]
for i in range(len(a)):
	if (a[i]-int("".join(list(str(a[i]))[::-1])))==81:
		print a[i]


