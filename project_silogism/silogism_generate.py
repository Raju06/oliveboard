import numpy as np
import random


def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x


class setClass:
	
	def __init__(self,oldSet):
		self.oldSet=oldSet

	def print1(self):
		return self.oldSet

	def intersect(self,newSet):
		intersectSet=[]
		for x in self.oldSet:
			if x in newSet:
				intersectSet.append(x)
		return intersectSet

	def subtract(self,newSet):
		subtractSet=[]
		for x in self.oldSet:
			if x not in newSet:
				subtractSet.append(x)
		return subtractSet
	
def checkValidity(oldSet,newSet,relation):
	oldSet=setClass(oldSet)
	if relation=='someAre':
		if len(oldSet.intersect(newSet))!=0:
			return True
		else:
			return False

	elif relation=='allAre':
		if set(oldSet.intersect(newSet))==set(oldSet.print1()):
			return True
		else:
			return False

	elif relation=='noAre':
		if len(oldSet.intersect(newSet))==0:
			return True
		else:
			return False

def createBinarySet(leftSet,rightSet,relation):
	alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if len(leftSet)==0:
		leftSet=list(np.random.choice(alphabets,random.choice([5,6,7]),replace=False))
	if relation=='all':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=leftSet+list(np.random.choice(newAlphabets,random.choice([3,4,5]),replace=False))
	elif relation=='some':
		commonAlphabets=list(np.random.choice(leftSet,random.choice([2,3,4]),replace=False))
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=commonAlphabets+list(np.random.choice(newAlphabets,random.choice([3,4,5]),replace=False))
	elif relation=='no':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=list(np.random.choice(newAlphabets,random.choice([5,6,7]),replace=False))
	else:
		pass
	return leftSet,rightSet


def createIndex():
	indexList=[]
	unusedQueue=shuffle(range(5))
	usedQueue=[unusedQueue.pop()]
	while len(unusedQueue)!=0:
		j=random.choice(usedQueue)
		k=unusedQueue.pop()
		usedQueue.append(k)
		indexList.append([j,k])
	return indexList

def createQuestionIndex(indexList):
	questionIndex={}
	for sublist in indexList:
		for i in range(len(sublist)):
			if sublist[i] in questionIndex.keys():
				questionIndex[sublist[i]].append(sublist[abs(len(sublist)-i-1)])
			else:
				questionIndex[sublist[i]]=[sublist[abs(len(sublist)-i-1)]]	
	return questionIndex

def createQuestion(questionIndex):
	itemRange=range(len(questionIndex))
	item=random.choice(itemRange)
	unusedRelation=[x for x in itemRange if x not in questionIndex[item]]
	return [setNames[item],setNames[random.choice(unusedRelation)],random.choice(['allAre','someAre','noAre'])]

def main():
	indexList=createIndex()
	questionIndex=createQuestionIndex(indexList)
	global setNames
	setNames={0:[],1:[],2:[],3:[],4:[]}
	relationList=[]
	for i in range(len(indexList)):
		relationList.append(random.choice(['all','some','no']))
		setNames[indexList[i][0]],setNames[indexList[i][1]]=createBinarySet(setNames[indexList[i][0]],setNames[indexList[i][1]],relationList[i])
	for key in setNames.keys():
		print key,'--->',setNames[key]
	questionList=[]
	questionList.append(createQuestion(questionIndex))
	questionList.append(createQuestion(questionIndex))
	questionList.append(createQuestion(questionIndex))
	return indexList,relationList,questionList

def createTruthTable(indexList,relationList,questionList,truthTable):
	setNames={0:[],1:[],2:[],3:[],4:[]}
	for i in range(len(indexList)):
		setNames[indexList[i][0]],setNames[indexList[i][1]]=createBinarySet(setNames[indexList[i][0]],setNames[indexList[i][1]],relationList[i])
	for key in setNames.keys():
		print key,'--->',setNames[key]
	for i in range(len(questionList)):
		truthTable[i].append(checkValidity(questionList[i][0],questionList[i][1],questionList[i][2]))
	return truthTable


indexList,relationList,questionList=main()
truthTable=[[],[],[]]
for i in range(10):
	indexList=shuffle(indexList)
	truthTable=createTruthTable(indexList,relationList,questionList,truthTable)
print questionList
print truthTable