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



def createBinarySet(leftSet,rightSet,relation):
	alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	print relation
	if len(leftSet)==0:
		leftSet=list(np.random.choice(alphabets,5,replace=False))
	if relation=='all':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=leftSet+list(np.random.choice(newAlphabets,3,replace=False))
	elif relation=='some':
		commonAlphabets=list(np.random.choice(leftSet,2,replace=False))
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=commonAlphabets+list(np.random.choice(newAlphabets,3,replace=False))
	elif relation=='no':
		newAlphabets=[x for x in alphabets if x not in leftSet]
		rightSet=list(np.random.choice(newAlphabets,5,replace=False))
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


indexList=createIndex()
print indexList

setNames={0:[],1:[],2:[],3:[],4:[]}
for i in range(len(indexList)):
	setNames[indexList[i][0]],setNames[indexList[i][1]]=createBinarySet(setNames[indexList[i][0]],setNames[indexList[i][1]],random.choice(['all','some','no']))
for key in setNames.keys():
	print key,'--->',setNames[key]
