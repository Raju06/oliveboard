import numpy as np
import random

def findRelation(args):
	currentNode='me'
	for item in args:
		currentNode=relationDict[currentNode][item]
	return currentNode


me=['male']
if me[0]=='male':
	relationDict={
	'grandfather':{'son':'father','daughter':'sister','father':None,'mother':None,'brother':None,'sister':None,'wife':'grandmother','husband':None},
	'grandmother':{'son':'father','daughter':'sister','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'grandfather'},
	'mother-in-law':{'son':'brother-in-law','daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'father-in-law'},
	'father-in-law':{'son':'brother-in-law','daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':'mother-in-law','husband':None},
	'husband':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':None},
	'wife':{'son':'son','daughter':'daughter','father':'father-in-law','mother':'mother-in-law','brother':'brother-in-law','sister':'sister-in-law','wife':None,'husband':'me'},
	'son':{'son':'grand-son','daughter':'grand-daughter','father':'me','mother':'wife','brother':None,'sister':'daughter','wife':'daughter-in-law','husband':None},
	'daughter':{'son':'grand-son','daughter':'grand-daughter','father':'me','mother':'wife','brother':'son','sister':None,'wife':None,'husband':'son-in-law'},
	'father':{'son':'me','daughter':'sister','father':'grandfather','mother':'grandmother','brother':'uncle','sister':'aunt','wife':'mother','husband':None},
	'mother':{'son':'me','daughter':'sister','father':None,'mother':None,'brother':'uncle','sister':'aunt','wife':None,'husband':'father'},
	'brother':{'son':None,'daughter':None,'father':'father','mother':'mother','brother':None,'sister':'sister','wife':'sister-in-law','husband':None},
	'sister':{'son':'nephew','daughter':'niece','father':'father-in-law','mother':'mother','brother':None,'sister':None,'wife':None,'husband':'brother-in-law'},
	'brother-in-law':{'son':'nephew','daughter':'niece','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':None},
	'sister-in-law':{'son':None,'daughter':None,'father':None,'mother':None,'brother':'brother-in-law','sister':None,'wife':None,'husband':None},
	'son-in-law':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':None,'sister':None,'wife':'daughter','husband':None},
	'daughter-in-law':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'son'},
	'grand-son':{'son':None,'daughter':None,'father':'son','mother':'daughter-in-law','brother':None,'sister':'grand-daughter','wife':None,'husband':None},
	'grand-daughter':{'son':None,'daughter':None,'father':'son','mother':'daughter-in-law','brother':'grand-son','sister':None,'wife':None,'husband':None},
	'uncle':{'son':'brother-in-law','daughter':'sister-in-law','father':None,'mother':None,'brother':None,'sister':None,'wife':'aunt','husband':None},
	'aunt':{'son':'brother-in-law','daughter':'sister-in-law','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'uncle'},
	'nephew':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':'niece','wife':None,'husband':None},
	'niece':{'son':None,'daughter':None,'father':None,'mother':None,'brother':'nephew','sister':None,'wife':None,'husband':None},
	'me':{'son':'son','daughter':'daughter','father':'father','mother':'mother','brother':'brother','sister':'sister','wife':'wife','husband':None}
	}



def opposite(relation,currentNode):
	if currentNode in ['father-in-law','nephew','grand-son','father','uncle','brother-in-law','son','me','son-in-law','brother','grandfather','husband']:
		if relation=='son':
			return 'father'
		elif relation=='daughter':
			return 'father'
		elif relation=='wife':
			return 'husband'
		elif relation=='father':
			return 'son'
		elif relation=='mother':
			return 'son'
		elif relation=='brother':
			return 'brother'
		elif relation=='sister':
			return 'brother'	
		else:
			return error
	else:
		if relation=='son':
			return 'mother'
		elif relation=='daughter':
			return 'mother'
		elif relation=='husband':
			return 'wife'
		elif relation=='father':
			return 'daughter'
		elif relation=='mother':
			return 'daughter'
		elif relation=='brother':
			return 'sister'
		elif relation=='sister':
			return 'sister'
		else:
			return error



def createExpression():
	capitals=[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
	members=list(np.random.choice(capitals,6,replace=False))
	expression=''
	relationsList=['son','daughter','father','mother','brother','sister','wife']
	currentNode='me'
	nodeDict={}
	i=0
	while i<6:
		relative_currentNode=currentNode
		relation=random.choice(relationsList)	
		member=random.choice(members)
		if member not in nodeDict.keys():
			nodeDict[member]={}
		while relation in nodeDict[member].keys() or relationDict[currentNode][relation] == None:
			relation=random.choice(relationsList)
		currentNode=relationDict[currentNode][relation]
		relative=random.choice(members)
		while relative ==member or relative in nodeDict[member].values():
			relative=random.choice(members)
		nodeDict[member][relation]=relative
		if relative not in nodeDict.keys():
			nodeDict[relative]={}
		nodeDict[relative][opposite(relation,relative_currentNode)]=member
		expression+='{} {} {},'.format(relative,relation,member)
		i+=1
	return expression,nodeDict


print createExpression()
#args=raw_input('Enter relations: ').split()
#print findRelation(args)