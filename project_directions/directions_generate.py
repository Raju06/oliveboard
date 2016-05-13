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


def createExpression():
	global q
	symbolDict=createRules()
	digitDict={'alphabets':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],'numbers':['1','2','3','4','5','6','7','8','9'],'capitals':[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]}
	if random.choice([0,1,2])==0:
		q=shuffle(digitDict['alphabets'])[:5]
	elif random.choice([0,1,2])==1:
		q=shuffle(digitDict['numbers'])[:5]
	else:
		q=shuffle(digitDict['capitals'])[:5]
	digitList=[[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[3],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[2],q[3]],[q[1],q[4]]],[[q[0],q[1]],[q[1],q[2]],[q[1],q[3]],[q[1],q[4]]]]
	binaryPair=list(digitList[random.randrange(0,3)])
	avoidDuplicate={}
	for item in q:
		avoidDuplicate[item]=[]
	relationList=[]
	for i in range(len(binaryPair)):
		relation=random.choice([x for x in directionsList if x not in avoidDuplicate[binaryPair[i][0]] and x not in avoidDuplicate[binaryPair[i][1]]])
		avoidDuplicate[binaryPair[i][1]].append(relation)
		avoidDuplicate[binaryPair[i][0]].append(oppositeDirections[relation])
		relationList.append(relation)

	return binaryPair,relationList

print createExpression()