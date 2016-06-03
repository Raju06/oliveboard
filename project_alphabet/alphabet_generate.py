import random,os
import numpy as np
import itertools

def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

def getWord():
	global fh
	tempfh = os.path.join(os.path.dirname(__file__), 'samplewords.txt')
	fh = open(tempfh, "r")
	for line in fh:
		samplewords=line.split()
	
	word =random.choice(samplewords)
	while len(word)<7:
		word=random.choice(samplewords)
	return word

def getResult(word):
	global letters
	letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	resultList=[]
	for i in range(len(word)):
		for j in range(i+1,len(word)):
			if letters.index(word[j])-letters.index(word[i])==j-i or letters.index(word[j])-letters.index(word[i])==i-j:
				resultList.append(str(word[i]+word[j]))

	return resultList

def createText(word,resultList):
	
	answer=len(resultList)
	tempOptionsList=[answer,answer+1,answer+2,answer+3,answer+4,answer+5,answer-1,answer-2,answer-3]
	optionsList=[]
	for item in tempOptionsList:
		if item<0:
			item=item*-1
		if item not in optionsList and item!=answer:
			optionsList.append(item)
	options=list(np.random.choice(optionsList,4,replace=False))
	options.append(answer)
	options=shuffle(options)

	text='How many such pairs of letters are there in the word \'{}\' each of which has as many letters between them in the word as in the English alphabet?\n'.format(word)
	text+='(1){}\n(2){}\n(3){}\n(4){}\n(5){}\nAnswer Key: {}\nSolution:\n'.format(options[0],options[1],options[2],options[3],options[4],options.index(answer)+1)
	for letter in word:
		text+='{} - {}\n'.format(letter,letters.index(letter)+1)

	text+='The pairs are: {}\n'.format(', '.join(resultList))
	text+='Hence {} such pairs'.format(len(resultList))

	return text
	


countFinal=input('Enter number of questions to be written : ')
sets_count=0
while sets_count<countFinal:
	#try:
	
	text=str('\n\n{}. ').format(sets_count+1)
	word=getWord()
	resultList=getResult(word)
	text+=str(createText(word,resultList))
	#print "Set {}".format(i+1)
	global fn
	fn = os.path.join(os.path.dirname(__file__), 'sampleQuestions.txt')
	file = open(fn, "a")
 	file.write(text)
 	file.close()
 	sets_count+=1
	#except:
	#	print ('\n')+"Error in Set {}".format(sets_count+1)
	#	pass
print 'Done. Output written to file : {} '.format(fn)
