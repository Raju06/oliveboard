import numpy as np
import random

def findRelation(args):
	currentNode='me'
	for item in args:
		currentNode=relationDict[currentNode][item]
	return currentNode


me=['male']
if me[0]=='male':
	relationDict={'grandfather':{'son':'father','daughter':'sister','father':None,'mother':None,'brother':None,'sister':None,'wife':'grandmother','husband':None},
	'grandmother':{'son':'father','daughter':'sister','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'grandfather'},
	'mother-in-law':{'son':'brother-in-law','daughter':'wife','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'father-in-law'},
	'father-in-law':{'son':'brother-in-law','daughter':'wife','father':None,'mother':None,'brother':None,'sister':None,'wife':'mother-in-law','husband':None},
	'husband':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':None},
	'wife':{'son':'son','daughter':'daughter','father':None,'mother':None,'brother':'brother-in-law','sister':'sister-in-law','wife':None,'husband':'me'},
	'son':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':None,'sister':'daughter','wife':'daughter-in-law','husband':None},
	'daughter':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':'son','sister':None,'wife':None,'husband':'son-in-law'},
	'father':{'son':'me','daughter':'sister','father':None,'mother':None,'brother':'uncle','sister':'aunt','wife':'mother','husband':None},
	'mother':{'son':'me','daughter':'sister','father':None,'mother':None,'brother':'uncle','sister':None,'wife':None,'husband':'father'},
	'brother':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':'sister-in-law','husband':None},
	'sister':{'son':'nephew','daughter':'niece','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'brother-in-law'},
	'brother-in-law':{'son':'nephew','daughter':'niece','father':None,'mother':None,'brother':None,'sister':'wife','wife':None,'husband':None},
	'sister-in-law':{'son':None,'daughter':None,'father':None,'mother':None,'brother':'brother-in-law','sister':'wife','wife':None,'husband':None},
	'son-in-law':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':None,'sister':None,'wife':'daughter','husband':None},
	'daughter-in-law':{'son':'grand-son','daughter':'grand-daughter','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'son'},
	'grand-son':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':'grand-daughter','wife':None,'husband':None},
	'grand-daughter':{'son':None,'daughter':None,'father':None,'mother':None,'brother':'grand-son','sister':None,'wife':None,'husband':None},
	'uncle':{'son':'brother-in-law','daughter':'sister-in-law','father':None,'mother':None,'brother':None,'sister':None,'wife':'aunt','husband':None},
	'aunt':{'son':'brother-in-law','daughter':'sister-in-law','father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':'uncle'},
	'nephew':{'son':None,'daughter':None,'father':None,'mother':None,'brother':None,'sister':None,'wife':None,'husband':None},
	'me':{'son':'son','daughter':'daughter','father':None,'mother':None,'brother':'brother','sister':'sister','wife':'wife','husband':None}}

def createExpression():
	capitals=[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
	members=list(np.random.choice(capitals,6,replace=False))
	expression=''
	relationsList=['son','daughter','father','mother','brother','sister','wife']
	currentNode='me'
	i=0
	while i<6:
		relation=random.choice(relationsList)
		if relationDict[currentNode][relation]!= None:
			currentNode=relationDict[currentNode][relation]
			expression+='{} {} '.format(members.pop(),relation)
			i+=1
		else:
			print "Hola"
	return expression



print createExpression()
#args=raw_input('Enter relations: ').split()
#print findRelation(args)