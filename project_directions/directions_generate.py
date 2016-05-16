import numpy as np
import random,time,os
from itertools import combinations
from itertools import permutations

def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

def createRules():
	global symbolList,directions,oppositeDirections,directionsList
	symbolList=list(np.random.choice(['*','@','#','$','%','^','&'],5,replace=False))
	directions=['N','E','S','W','NE','NW','SE','SW']
	oppositeDirections={'N':'S','E':'W','S':'N','W':'E','NE':'SW','NW':'SE','SE':'NW','SW':'NE'}
	directionsList=list(np.random.choice(directions,5,replace=False))
	symbolDict={directionsList[0]:symbolList[0],directionsList[1]:symbolList[1],directionsList[2]:symbolList[2],directionsList[3]:symbolList[3],directionsList[4]:symbolList[4]}
	return symbolDict

def checkRelation(itemList):
	resultDict={('N', 'SW'): ['W', 'NW', 'SW'], ('S', 'W'): ['SW'], ('S', 'SW'): ['SW'], ('E', 'S'): ['SE'], ('N', 'SE'): ['E', 'NE', 'SE'], ('NE', 'SE'): ['E', 'NE', 'SE'], ('E', 'W'): ['W','E'], ('NW', 'SE'): ['NW','SE'], ('W', 'SE'): ['S', 'SE', 'SW'], ('N', 'NE'): ['NE'], ('N', 'NW'): ['NW'], ('NW', 'SW'): ['W', 'NW', 'SW'], ('N', 'S'): ['N','S'], ('W', 'SW'): ['SW'], ('N', 'E'): ['NE'], ('E', 'NW'): ['N', 'NW', 'NE'], ('SE', 'SW'): ['S', 'SE', 'SW'], ('N', 'W'): ['NW'], ('NE', 'SW'): ['NE','SW'], ('E', 'NE'): ['NE'], ('S', 'NW'): ['W', 'NW', 'SW'], ('E', 'SE'): ['SE'], ('S', 'NE'): ['E', 'NE', 'SE'], ('NE', 'NW'): ['N', 'NE', 'NW'], ('W', 'NE'): ['N', 'NW', 'NE'], ('E', 'SW'): ['S', 'SE', 'SW'], ('S', 'SE'): ['SE'], ('W', 'NW'): ['NW'],('N', 'N'): ['N'],('E', 'E'): ['E'],('S', 'S'): ['S'],('W', 'W'): ['W'],('NE', 'NE'): ['NE'],('NW', 'NW'): ['NW'],('SE', 'SE'): ['SE'],('SW', 'SW'): ['SW'],('0', 'N'): ['0'],('0', 'S'): ['0'],('0', 'W'): ['0'],('0', 'E'): ['0'],('0', 'NE'): ['0'],('0', 'SE'): ['0'],('0', 'NW'): ['0'],('0', 'SW'): ['0']}
	tempDict={}
	for item in resultDict:
		tempitem=item[::-1]
		tempDict[tempitem]=resultDict[item]
	resultDict.update(tempDict)
	return resultDict[tuple(itemList)]

def createQuestion(binaryPair):
	conditionMet=False
	question=list(np.random.choice(q,2,replace=False))
	while not conditionMet:
		if question in binaryPair or question[::-1] in binaryPair:
			question=list(np.random.choice(q,2,replace=False))
		else:
			conditionMet=True
	return question

def createSolution(question,binaryPair,relationList):
	solutionChain=[]
	for item in relationChain:
		if question[0] in item and question[1] in item:
			if item.index(question[0])<item.index(question[1]):
				questionChain=item[item.index(question[0]):item.index(question[1])+1]
			else:
				questionChain=item[item.index(question[1]):item.index(question[0])+1][::-1]

	start=0
	print questionChain
	while start<len(questionChain)-1:
		if [questionChain[start],questionChain[start+1]] in binaryPair:
			solutionChain.append(oppositeDirections[relationList[binaryPair.index([questionChain[start],questionChain[start+1]])]])
		elif [questionChain[start+1],questionChain[start]] in binaryPair:
			solutionChain.append(relationList[binaryPair.index([questionChain[start+1],questionChain[start]])])
		start+=1

	print solutionChain
	tempList=checkRelation([solutionChain[0],solutionChain[1]])
	solutionList=tempList
	start=2
	while start<len(solutionChain):
		solutionList=[]
		for item in tempList:
			alist=checkRelation([item,solutionChain[start]])
			for alistItem in alist:
				if alistItem not in solutionList:
					solutionList.append(alistItem)
		tempList=solutionList
		start+=1

	print solutionList




def createExpression():
	global q,relationChain
	symbolDict=createRules()
	digitDict={'alphabets':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],'numbers':['1','2','3','4','5','6','7','8','9'],'capitals':[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]}
	if random.choice([0,1,2])==0:
		q=shuffle(digitDict['alphabets'])[:5]
	elif random.choice([0,1,2])==1:
		q=shuffle(digitDict['numbers'])[:5]
	else:
		q=shuffle(digitDict['capitals'])[:5]
	digitList=[[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[3],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[1],q[3]],[q[1],q[4]]]]
	selection=random.randrange(0,3)
	binaryPair=list(digitList[selection])
	if selection==0:
		relationChain=[[x for x in q]]
	elif selection==1:
		relationChain=[q[0],q[1],q[4]],[q[0],q[1],q[2],q[3]],[q[4],q[1],q[2],q[3]]
	else:
		relationChain=[q[0],q[1],q[3]],[q[0],q[1],q[4]],[q[0],q[1],q[2]],[q[3],q[1],q[2]],[q[3],q[1],q[4]],[q[4],q[1],q[2]]
	avoidDuplicate={}
	for item in q:
		avoidDuplicate[item]=[]
	relationList=[]
	for i in range(len(binaryPair)):
		relation=random.choice([x for x in directionsList if x not in avoidDuplicate[binaryPair[i][0]] and x not in avoidDuplicate[binaryPair[i][1]]])
		avoidDuplicate[binaryPair[i][1]].append(oppositeDirections[relation])
		avoidDuplicate[binaryPair[i][0]].append(relation)
		relationList.append(relation)
	return binaryPair,relationList

binaryPair,relationList=createExpression()
print binaryPair,relationList
question=createQuestion(binaryPair)
print question
createSolution(question,binaryPair,relationList)