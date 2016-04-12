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
	
def checkValidity(oldSetIndex,newSetIndex,relation):
	oldSet=setNamesTruth[oldSetIndex]
	newSet=setNamesTruth[newSetIndex]
	oldSet=setClass(oldSet)
	if relation=='someAre':
		if len(oldSet.intersect(newSet))!=0:
			return 1
		else:
			return 0

	elif relation=='allAre':
		if set(oldSet.intersect(newSet))==set(oldSet.print1()):
			return 1
		else:
			return 0

	elif relation=='noAre':
		if len(oldSet.intersect(newSet))==0:
			return 1
		else:
			return 0

def createBinarySet(leftSet,rightSet,relation):
	alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	capitals=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	alphabets=alphabets+capitals
	if len(leftSet)==0:
		leftSet=list(np.random.choice(alphabets,random.choice([4,5,6,7]),replace=False))
	if relation=='all':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=leftSet+list(np.random.choice(newAlphabets,random.choice([3,4]),replace=False))
	elif relation=='some':
		commonAlphabets=list(np.random.choice(leftSet,random.choice([2,3,4]),replace=False))
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=commonAlphabets+list(np.random.choice(newAlphabets,random.choice([3,4]),replace=False))
	elif relation=='no':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=list(np.random.choice(newAlphabets,random.choice([4,5,6,7]),replace=False))
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
	unusedRelation=[x for x in itemRange if x not in questionIndex[item] and x != item]
	return [item,random.choice(unusedRelation),random.choice(['allAre','someAre','noAre'])]

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
	while len(questionList)!=3:
		tempMain=createQuestion(questionIndex)
		if tempMain not in questionList:
			questionList.append(tempMain)
	return indexList,relationList,questionList

def createTruthTable(indexList,relationList,questionList,truthTable):
	global setNamesTruth
	setNamesTruth={0:[],1:[],2:[],3:[],4:[]}
	for i in range(len(indexList)):
		setNamesTruth[indexList[i][0]],setNamesTruth[indexList[i][1]]=createBinarySet(setNamesTruth[indexList[i][0]],setNamesTruth[indexList[i][1]],relationList[i])
	for i in range(len(questionList)):
		tempTruth=checkValidity(questionList[i][0],questionList[i][1],questionList[i][2])
		truthTable[i]+=tempTruth
	return truthTable


indexList,relationList,questionList=main()
truthTable=[0,0,0]
for i in range(10000):
	truthTable=createTruthTable(indexList,relationList,questionList,truthTable)
print indexList,relationList,questionList
for i in range(3):
	print truthTable[i]


