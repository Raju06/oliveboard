from itertools import permutations
from itertools import combinations
import numpy as np
import random,time

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

def checkValidity(exp):
	resultList=[]
	for i in range(len(finalList)):
		if exp[0] in finalList[i] and exp[2] in finalList[i]:
			
			firstIndex=finalList[i].index(exp[0])
			secondIndex=finalList[i].index(exp[2])
			if firstIndex<secondIndex:
				t= finalList[i][firstIndex:secondIndex+1]
			else:
				t= expressionOpposite(finalList[i][secondIndex:firstIndex+1])
			if t not in resultList and expressionOpposite(t) not in resultList:
				resultList.append(t)
	resultList=''.join(resultList)
	negationDict={'greaterThan':[symbolDict['lessThan'],symbolDict['lessThanEqualTo'],symbolDict['greaterThanEqualTo']],'greaterThanEqualTo':[symbolDict['lessThan'],symbolDict['lessThanEqualTo'],symbolDict['greaterThan']],'lessThan':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThanEqualTo']],'lessThanEqualTo':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThan']],'equalTo':[symbolDict['greaterThan'],symbolDict['greaterThanEqualTo'],symbolDict['lessThanEqualTo'],symbolDict['lessThan']]}
	resultSymbolList=[]
	indexResultList=1
	while indexResultList<len(resultList):
		resultSymbolList.append(resultList[indexResultList])
		indexResultList+=2
	symbolDictReverse=dict((v, k) for k, v in symbolDict.items())
	returnValue=True
	for i in range(len(resultSymbolList)):
		if resultSymbolList[i] in negationDict[symbolDictReverse[exp[1]]]:
			returnValue=False
	if len(resultSymbolList)==0:
		returnValue=False
	return returnValue

def createExpression():
	digitDict={'alphabets':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	,'numbers':['1','2','3','4','5','6','7','8','9'],'capitals':[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]}
	global q,inputSymbols
	inputSymbols=list(np.random.choice(symbolList,4))
	
	tempcreateExpression=random.randrange(0,3)
	if tempcreateExpression == 0:
		q=shuffle(digitDict['alphabets'])[:6]
	elif tempcreateExpression==1:
		q=shuffle(digitDict['numbers'])[:6]
	else:
		q=shuffle(digitDict['capitals'])[:6]
	digitList=[[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[3],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[1],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[4],q[5]]],[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[3],q[5]]],[[q[0],q[1]],[q[1],q[2]],[q[3],q[4]],[q[3],q[5]]]]
	binaryPair=list(digitList[random.randrange(0,6)])
	binaryPair=shuffle(binaryPair)
	inputExpression=''
	for i in range(len(binaryPair)):
		inputExpression+=str(binaryPair[i][0]+inputSymbols[i]+binaryPair[i][1])+str(',')
	
	return inputExpression[:len(inputExpression)-1]

def createQuestion(condition):
	conditionMet=False
	question=''
	while not conditionMet or question in expression_list or expressionOpposite(question) in expression_list:
		variables=list(np.random.choice(q,2,replace=False))
		symbol=random.choice(inputSymbols)
		question=str(variables[0]+symbol+variables[1])
		conditionMet=(condition==checkValidity(question))
		time.sleep(.05)
		print question
	return question

#symbolList=list(np.random.choice(['*','@','#','$','%','^','&'],5,replace=False))
#symbolList=shuffle(symbolList)
symbolList=['*','@','#','$','%']
symbolDict={'equalTo':symbolList[0],'greaterThan':symbolList[1],'greaterThanEqualTo':symbolList[2],'lessThan':symbolList[3],'lessThanEqualTo':symbolList[4]}
for key in symbolDict.keys():
	print key,' is represented as ',symbolDict[key]

expression_list=createExpression().split(',')
print expression_list
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
				if temp in alist[j] or alist[j] in temp:
					found=True
					break
			if not found:
				alist.append(temp)
	finalList=[]					
	for i in range(len(alist)):
		if expressionOpposite(alist[i]) not in finalList:
			finalList.append(alist[i])
	return finalList

finalList= main(expression_list)
print finalList
print createQuestion(True)