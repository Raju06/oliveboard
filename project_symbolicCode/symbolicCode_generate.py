# -*- coding: utf-8 -*-

import numpy as np
import random,itertools,os



def createRepresentation():
	capitals=[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
	evenNumbers=['0','2','4','6','8']
	oddNumbers=['1','3','5','7','9']
	vowels=['A','E','I','O','U']
	consonants=[x for x in capitals if x not in vowels]
	symbols=['!','@','#','$','%','^','&','*','?','~','{','}','<','>','|']
	
	capitalsList=list(np.random.choice(capitals,7,replace=False))
	evenNumbersList=list(np.random.choice(evenNumbers,3,replace=False))
	oddNumbersList=list(np.random.choice(oddNumbers,3,replace=False))
	symbolsList=list(np.random.choice(symbols,13,replace=False))
	lettersList=capitalsList+evenNumbersList+oddNumbersList
	representationList={}
	for i in range(13):
		representationList[lettersList[i]]=symbolsList[i]
	return representationList
