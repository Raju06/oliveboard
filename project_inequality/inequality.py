def generateMatrix():
	matrix=[['.' for j in range(80)] for i in range(80)]
	for i in range(len(a)):
		#print ' '.join(a[i])
		pass


expression=raw_input('Enter the expression separated by , :').split(',')
print expression
expression_list=[]
for i in range(len(expression)):
	expression_list.append(['','',''])
	for j in range(len(expression[i])):
		if expression[i][j] in ['>','<','=']:
			expression_list[i][2]+=expression[i][j]
		else:
			expression_list[i]=expression[i][j]

#for i in range(len(expression_list)):

generateMatrix()