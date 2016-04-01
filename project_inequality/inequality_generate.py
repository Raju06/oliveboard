import numpy as np
import random,time
from itertools import combinations
from itertools import permutations




def mainProgram():
	text=''
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
		if len(exp)==0:
			return ''
		else:
			expression=''
			i=0
			while i<len(exp)-2:
				expression+=exp[len(exp)-i-1]+opposite(exp[len(exp)-i-2])
				i+=2
			return expression+exp[0]

	def filter_list(L):
	    return [x for x in L if not any(set(x)<=set(y) for y in L if x is not y)]


	def createRelations(text):
		global symbolList,symbolDict
		text+='Consider the following:\n'
		symbolList=list(np.random.choice(['*','@','#','$','%','^','&'],5,replace=False))
		symbolList=shuffle(symbolList)
		#symbolList=['*','@','#','$','%']
		symbolDict={'equalTo':symbolList[0],'greaterThan':symbolList[1],'greaterThanEqualTo':symbolList[2],'lessThan':symbolList[3],'lessThanEqualTo':symbolList[4]}
		symbolDictNotation={'is neither smaller nor greater than':symbolList[0],'is neither smaller nor equal to':symbolList[1],'is not smaller than':symbolList[2],'is neither greater nor equal to':symbolList[3],'is not greater than':symbolList[4]}
		for key in symbolDictNotation.keys():
			text+='\'A{}B\' means \'A {} B\'\n'.format(symbolDictNotation[key],key)
		text+='Now in each of the following questions, assuming the given statements to be true, find which of the two conclusions given below them is/are false. Give answer\n'
		return text

	text=createRelations(text)


	def createExpression():
		digitDict={'alphabets':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		,'numbers':['1','2','3','4','5','6','7','8','9'],'capitals':[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]}
		global q,inputSymbols
		inputSymbols=list(np.random.choice(symbolList,4))
		tempcreateExpression=random.randrange(0,3)
		levelType=random.randrange(1,3)
		if tempcreateExpression == 0:
			if levelType==1:
				q=shuffle(digitDict['alphabets'])[:5]
			else:
				q=shuffle(digitDict['alphabets'])[:6]
		elif tempcreateExpression==1:
			if levelType==1:
				q=shuffle(digitDict['numbers'])[:5]
			else:
				q=shuffle(digitDict['numbers'])[:6]
		else:
			if levelType==1:
				q=shuffle(digitDict['capitals'])[:5]
			else:
				q=shuffle(digitDict['capitals'])[:6]
		if levelType==1:
			digitList=[[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[3],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[1],q[3]],[q[1],q[4]]]]
		else:
			digitList=[[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[4],q[5]]],[[q[0],q[1]],[q[2],q[3]],[q[3],q[4]],[q[3],q[5]]],[[q[0],q[1]],[q[1],q[2]],[q[3],q[4]],[q[3],q[5]]]]	
		binaryPair=list(digitList[random.randrange(0,3)])
		binaryPair=shuffle(binaryPair)
		inputExpression=''
		for i in range(len(binaryPair)):
			inputExpression+=str(binaryPair[i][0]+inputSymbols[i]+binaryPair[i][1])+str(',')
		
		return inputExpression[:len(inputExpression)-1]


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


	def createQuestion(condition):
		global infiniteLoopCount
		infiniteLoopCount=0
		conditionMet=False
		question=''
		while not conditionMet:
			variables=list(np.random.choice(q,2,replace=False))
			symbol=random.choice(inputSymbols)
			question=str(variables[0]+symbol+variables[1])
			conditionMet=(condition==checkValidity(question))
			for i in range(len(symbolList)):
				if str(question[0]+symbolList[i]+question[2]) in expression_list or str(question[2]+symbolList[i]+question[0]) in expression_list :
					conditionMet=False
			if infiniteLoopCount==100:
				break
			infiniteLoopCount+=1

			#print question
		return question


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

	def createQuestionsList():
		count=0
		questionList=[]
		answerList=[]

		while count<2:


			answerListTemp=random.choice([True,False])
			questionListTemp=createQuestion(answerListTemp)
			if infiniteLoopCount<100:
				toAdd=True
				for i in range(len(inputSymbols)):
					if (str(questionListTemp[0]+inputSymbols[i]+questionListTemp[2]) in questionList) or (str(questionListTemp[2]+inputSymbols[i]+questionListTemp[0]) in questionList):
						toAdd=False
				if toAdd:
					questionList.append(questionListTemp)
					answerList.append(answerListTemp)
					count+=1
		return questionList,answerList




	def subMain():
		expression_list=createExpression().split(',')
		finalList= main(expression_list)
		return expression_list,finalList


	finalList_main=[]
	expression_list_main=[]
	i=0
	while i<5:
		expression_list,finalList=subMain()
		questionList,answerList=createQuestionsList()
		if infiniteLoopCount<100:
			finalList_main.append(finalList)
			expression_list_main.append(expression_list)	
			i+=1
			text+='\n{}.Statement:\n{}\nConclusion:\nI. {}\nII. {}\n(1) If only conclusion I is false.\n(2) If only conclusion II is false.\n(3) If either conclusion I or II is false.\n(4) If neither conclusion I or II is false.\n(5) If both conclusion I and II are false.\n\nAnswers are\nI. {}\nII. {}\n'.format(i,', '.join(expression_list),questionList[0],questionList[1],answerList[0],answerList[1])
		else:
			print "Avoiding infiniteLoop"
	return text


countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	try:
		text=str('\nSet {}\n\n').format(sets_count+1)+mainProgram()
		#print "Set {}".format(i+1)
		file = open("C:\Users\Olive\Desktop\oliveboard\project_inequality\sampleQuestions.txt", "a")
	 	file.write(text)
	 	file.close()
	 	sets_count+=1
	except:
		print ('\n')+"Error in Set {}".format(sets_count+1)
		pass


			