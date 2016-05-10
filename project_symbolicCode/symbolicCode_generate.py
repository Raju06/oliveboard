# -*- coding: utf-8 -*-
import numpy as np
import random,itertools,os

capitals=[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
even=['0','2','4','6','8']
odd=['1','3','5','7','9']
vowels=['A','E','I','O','U']
consonants=[x for x in capitals if x not in vowels]

def createRepresentation():
	symbols=['!','@','#','$','%','^','&','*','?','~','{','}','<','>','|']
	symbolsList=list(np.random.choice(symbols,13,replace=False))
	lettersList=list(np.random.choice(vowels,3,replace=False))+list(np.random.choice(consonants,4,replace=False))+list(np.random.choice(even,3,replace=False))+list(np.random.choice(odd,3,replace=False))	
	representationList={}
	for i in range(13):
		representationList[lettersList[i]]=symbolsList[i]
	return representationList

def createRules():
	global rulesList
	rulesList=[]
	while len(rulesList)<3:
		index=list(np.random.choice([1,2,3,4,5,6],2,replace=False,p=[0.3,0.1,0.2,0.05,0.05,0.3]))
		index.sort()
		itemClass=list(np.random.choice(['vowels','consonants','even','odd'],2,replace=True))
		rule=index+itemClass
		if rule not in rulesList:
			rulesList.append(rule)
	return rulesList

def convertQuestion(questionCondition):
	question=''
	evenItems=list(np.random.choice(evenList,questionCondition.count('even'),replace=False))
	oddItems=list(np.random.choice(oddList,questionCondition.count('odd'),replace=False))
	vowelsItems=list(np.random.choice(vowelsList,questionCondition.count('vowels'),replace=False))
	consonantsItems=list(np.random.choice(consonantsList,questionCondition.count('consonants'),replace=False))
	tempList=[x for x in letterList if x not in evenItems+oddItems+vowelsItems+consonantsItems]
	letterItems=list(np.random.choice(tempList,questionCondition.count('letter'),replace=False))

	for condition in questionCondition:
		if condition=='even':
			question+=evenItems.pop()
		elif condition=='odd':
			question+=oddItems.pop()
		elif condition=='vowels':
			question+=vowelsItems.pop()
		elif condition=='consonants':
			question+=consonantsItems.pop()
		else:
			question+=letterItems.pop()

	return question


def checkNoRule(noRuleQuestion,rulesList):
	status=False
	itemDict={}
	itemDict['even']=evenList
	itemDict['odd']=oddList
	itemDict['vowels']=vowelsList
	itemDict['consonants']=consonantsList

	for item in rulesList:
		if noRuleQuestion[item[0]-1] in itemDict[item[2]] and noRuleQuestion[item[1]-1] in itemDict[item[3]]:
			status=True
			break

	return status

def createQuestion(rulesList,representationList):
	global vowelsList,consonantsList,evenList,oddList,letterList
	vowelsList=[]
	consonantsList=[]
	evenList=[]
	oddList=[]
	letterList=[]
	for key in representationList:
		letterList.append(key)
		if key in vowels:
			vowelsList.append(key)
		elif key in consonants:
			consonantsList.append(key)
		elif key in even:
			evenList.append(key)
		elif key in odd:
			oddList.append(key)
		else:
			pass

	questionList=[]
	questionConditionList=[]
	questionType=[]
	indexList=[0,1,2]
	indexList.append(random.choice([0,1,2]))
	while len(questionList)<4:
		index=indexList.pop()
		rule=rulesList[index]
		questionType.append(index+1)
		questionCondition=['letter' for i in range(6)]
		questionCondition[rule[0]-1]=rule[2]
		questionCondition[rule[1]-1]=rule[3]
		questionConditionList.append(questionCondition)
		questionList.append(convertQuestion(questionCondition))
	questionCondition=list(np.random.choice(['letter','even','odd','vowels','consonants'],6))
	noRuleQuestion=convertQuestion(questionCondition)
	while checkNoRule(noRuleQuestion,rulesList):
		questionCondition=list(np.random.choice(['letter','even','odd','vowels','consonants'],6))
		noRuleQuestion=convertQuestion(questionCondition)
	questionList.append(convertQuestion(questionCondition))
	
	return questionList

representationList=createRepresentation()
rulesList=createRules()
print representationList
print rulesList
print createQuestion(rulesList,representationList)







