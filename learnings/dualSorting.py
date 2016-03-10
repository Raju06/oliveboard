numberOfEntries=input('Enter the number of entries')
itemName=[]
customerRating=[]
price=[]
for i in range(numberOfEntries):
	itemName.append(raw_input('Enter the item name : '))
	customerRating.append(raw_input('Enter the customer rating for the item : '))
	price.append(raw_input('Enter the price of item : '))

table=[]
for i in range(numberOfEntries):
	k=[itemName[i],customerRating[i],price[i]]
	table.append(k)

finalTable=tuple(table)
table=list(table)

table.sort(key=lambda x:x[2])

finalTable=list(finalTable)
for i in range(len(finalTable)):
	found=False
	j=0
	while not found:
		if table[i][0]==finalTable[j][0]:
			finalTable[j].append(len(finalTable)-i)
			found=True
		else:
			j+=1
finalTable=tuple(finalTable)
table.sort(key=lambda x:x[1],reverse=True)
finalTable=list(finalTable)
for i in range(len(finalTable)):
	found=False
	j=0
	while not found:
		if table[i][0]==finalTable[j][0]:
			finalTable[j].append(len(finalTable)-i)
			found=True
		else:
			j+=1
for i in range(len(finalTable)):
	finalTable[i].append(finalTable[i][3]+finalTable[i][4])

finalTable.sort(key=lambda x:x[5],reverse=True)
for i in range(len(table)):
	print str(finalTable[i])