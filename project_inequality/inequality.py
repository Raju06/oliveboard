from itertools import permutations
import numpy as np

class expression:
	def  __init__(self):
		self.items=''

	def isEmpty(self):
		return self.items == ''

	def addRight(self, item):
		self.items+=item

	def addLeft(self, item):
		self.items=item+self.items
	
	def size(self):
		return len(self.items)

	def nothingToLeft(self,item):
		alist=[]
		for i in range(len(self.items)):
			if self.items[i]==item:
				alist.append(i)
		if 0 in alist:
			return True
		else:
			return False


	def nothingToRight(self,item):
		alist=[]
		for i in range(len(self.items)):
			if self.items[i]==item:
				alist.append(i)
		if len(self.items)-1 in alist:
			return True
		else:
			return False

	def returnExpression(self):
		return self.items

def shuffle(x):
	    x = list(x)
	    random.shuffle(x)
	    return x

def opposite(operator):

	symbolDict={'equalTo':symbolList[0],'greaterThan':symbolList[1],'greaterThanEqualTo':symbolList[2],'lessThan':symbolList[3],'lessThanEqualTo':symbolList[4]}
	if operator == symbolDict['greaterThan']:
		return symbolDict['lessThan']
	elif operator == symbolDict['greaterThanEqualTo']:
		return symbolDict['lessThanEqualTo']
	elif operator == symbolDict['equalTo']:
		return symbolDict['equalTo']
	elif operator == symbolDict['lessThan']:
		return symbolDict['greaterThan']
	elif operator == symbolDict['lessThanEqualTo']:
		return symbolDict['greaterThanEqualTo']

def expressionOpposite(exp):
	expression=''
	i=0
	while i<len(exp)-2:
		expression+=exp[len(exp)-i-1]+opposite(exp[len(exp)-i-2])
		i+=2
	return expression+exp[0]

def filter_list(L):
    return [x for x in L if not any(set(x)<=set(y) for y in L if x is not y)]


symbolList=[]
text=['equalTo','greaterThan','greaterThanEqualTo','lessThan','lessThanEqualTo']
for i in range(5):
	symbolList.append(raw_input('Enter symbol for : '+text[i]))
expression_list=raw_input('Enter the expression separated by comma(,) :').split(',')

def main(expression_list):
	def equation(expression_list):
		expression_list=list(expression_list)
		a=expression()
		a.addRight(expression_list.pop(0))
		for i in range(len(expression_list)):
			if expression_list[i][0] in a.returnExpression():
				if a.nothingToRight(expression_list[i][0]):
					a.addRight(expression_list[i][1:])
				elif a.nothingToLeft(expression_list[i][0]):
					expression_list[i]=expression_list[i][:1]+opposite(expression_list[i][1])+expression_list[i][2:]
					a.addLeft(expression_list[i][1:][::-1])
				else:
					pass
			elif expression_list[i][2] in a.returnExpression():
				if a.nothingToRight(expression_list[i][2]):
					expression_list[i]=expression_list[i][:1]+opposite(expression_list[i][1])+expression_list[i][2:]
					a.addRight(expression_list[i][:2][::-1])
				elif a.nothingToLeft(expression_list[i][2]):
					a.addLeft(expression_list[i][:2])
				else:
					pass
		return a.returnExpression()

	expression_list_new=[]
	alist=[]
	for c in permutations(expression_list):
		expression_list_new.append(list(c))

	for i in range(len(expression_list_new)):
		temp=equation(expression_list_new[i])
		if temp not in alist:
			found=False
			for j in range(len(alist)):
				if temp in alist[j]:
					found=True
					break
			if not found:
				alist.append(temp)
	finalList=[]					
	for i in range(len(alist)):
		if expressionOpposite(alist[i]) not in finalList:
			finalList.append(alist[i])
	return finalList

print main(expression_list)