import numpy as np
import random

def mainProgram():
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
		unusedQueue=shuffle(range(4))
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
		return [item,random.choice(unusedRelation),random.choice(['allAre','someAre','noAre','allArePossibility','someArePossibility','noArePossibility'])]

	def createWordsList():
		fh=open("C:\Users\Olive\Desktop\oliveboard\project_silogism\samplewords.txt", "r")
		for line in fh:
			samplewords=line.split()
		words_list=[]
		while len(words_list)<4:
			item_index=random.randrange(0,len(samplewords))
			if len(str(samplewords[item_index]))<6:
				#print "Hola"
				words_list.append(samplewords[item_index])
		return words_list

	def printText(questions,options):
		text='In this question three or four statements are given that may differ from the commonly known facts. Each statement is followed by three conclusions. You have to give correct answer out of the five options given below:\n\n'
		for i in range(5):
			text+='({}) Statement:\n{}\n{}\n{}\nConclusion:\n(I) {}\n(II) {}\n(III) {}\n(1) If only conclusion I and II follows but conclusion III do not follow\n(2) If only conclusion II and III follows but conclusion I do not follow\n(3) If only conclusion I and III follows but conclusion II do not follow\n(4) If all conclusion follows\n(5) If none conclusion follows\nAnswer key: \nSolution:\n\n'.format(i+1,questions[i][0],questions[i][1],questions[i][2],options[i][0],options[i][1],options[i][2])
		return text

	def createQuestionsText(indexList,relationList,wordsDict):
		questions=[]
		for i in range(len(relationList)):
			if relationList[i]=='all':
				questions.append('All {} are {}.'.format(wordsDict[indexList[i][0]],wordsDict[indexList[i][1]]))
			elif relationList[i]=='some':
				questions.append('Some {} are {}.'.format(wordsDict[indexList[i][0]],wordsDict[indexList[i][1]]))
			elif relationList[i]=='no':
				questions.append('No {} is {}.'.format(wordsDict[indexList[i][0]],wordsDict[indexList[i][1]]))
			else:
				pass
		return questions

	def createOptionsText(questionList,wordsDict):
		options=[]
		for i in range(len(questionList)):
			if questionList[i][2]=='allAre':
				options.append('All {} are {}.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			elif questionList[i][2]=='someAre':
				options.append('Some {} are {}.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			elif questionList[i][2]=='noAre':
				options.append('No {} is {}.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			elif questionList[i][2]=='allArePossibility':
				options.append('All {} being {} is a possibility.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			elif questionList[i][2]=='someArePossibility':
				options.append('Some {} being {} is a possibility.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			elif questionList[i][2]=='noArePossibility':
				options.append('No {} being {} is a possibility.'.format(wordsDict[questionList[i][0]],wordsDict[questionList[i][1]]))
			else:
				pass
		return options


	def main():
		indexList=createIndex()
		questionIndex=createQuestionIndex(indexList)
		global setNames
		setNames={0:[],1:[],2:[],3:[]}
		relationList=[]
		for i in range(len(indexList)):
			relationList.append(random.choice(['all','some','no']))
			setNames[indexList[i][0]],setNames[indexList[i][1]]=createBinarySet(setNames[indexList[i][0]],setNames[indexList[i][1]],relationList[i])
		questionList=[]
		while len(questionList)!=3:
			tempMain=createQuestion(questionIndex)
			if tempMain not in questionList:
				questionList.append(tempMain)
		return indexList,relationList,questionList


	indexList,relationList,questionList=main()
	questions=[]
	options=[]
	for i in range(5):
		wordsDict=dict(zip(range(4),createWordsList()))
		questions.append(createQuestionsText(indexList,relationList,wordsDict))
		options.append(createOptionsText(questionList,wordsDict))
	return printText(questions,options)


countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	try:
		text=str('\nSet {}\n\n').format(sets_count+1)+mainProgram()
		#print "Set {}".format(i+1)
		file = open("C:\Users\Olive\Desktop\oliveboard\project_silogism\sampleQuestions.txt", "a")
	 	file.write(text)
	 	file.close()
	 	sets_count+=1
	except:
		print ('\n')+"Error in Set {}".format(sets_count+1)
		pass