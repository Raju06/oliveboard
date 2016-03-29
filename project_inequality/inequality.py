def generateMatrix():
	matrix=[['.' for j in range(80)] for i in range(80)]
	for i in range(len(a)):
		#print ' '.join(a[i])
		pass

def mergeExpression(expression_dict):


expression=raw_input('Enter the expression separated by , :').split(',')
print expression
expression_dict={}
expression_dict['variables']=[]
expression_dict['operators']=[]
for i in range(len(expression)):
	expression_dict['variables'].append([])
	expression_dict['operators'].append([])
	for j in range(len(expression[i])):
		if expression[i][j] in ['>','<','=']:
			expression_dict['operators'][len(expression_dict['operators'])-1].append(expression[i][j])
		else:
			expression_dict['variables'][len(expression_dict['variables'])-1].append(expression[i][j])

#for i in range(len(expression_list)):
print expression_dict