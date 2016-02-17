maxl = len(l[0])
for i in range(1,len(l)):
    if len(l[i]) > maxl: maxl = len(l[i])

vals = []
for i in range(0,maxl):
    for j in range(0,len(l)):
        if len(l[j]) > i:
            vals.append(l[j][i])