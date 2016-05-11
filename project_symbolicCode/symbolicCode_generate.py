# -*- coding: utf-8 -*-
import numpy as np
import random,itertools,os

def main():
	capitals=[x.upper() for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
	even=['0','2','4','6','8']
	odd=['1','3','5','7','9']
	vowels=['A','E','I','O','U']
	consonants=[x for x in capitals if x not in vowels]

	def createRepresentation():
		symbols=['!','@','#','$','%','^','&','*','?','~','{','}','<','>','|']
		symbolsList=list(np.random.choice(symbols,13,replace=False))
		lettersList=list(np.random.choice(vowels,3,replace=False))+list(np.random.choice(consonants,4,replace=False))+list(np.random.choice(even,3,replace=False))+list(np.random.choice(odd,3,replace=False))	
		representationList={}
		for i in range(13):
			representationList[lettersList[i]]=symbolsList[i]
		return representationList

	def createRules():
		global rulesList
		rulesList=[]
		while len(rulesList)<3:
			index=list(np.random.choice([1,2,3,4,5,6],2,replace=False,p=[0.3,0.1,0.2,0.05,0.05,0.3]))
			index.sort()
			itemClass=list(np.random.choice(['vowels','consonants','even','odd'],2,replace=True))
			rule=index+itemClass
			if rule not in rulesList:
				rulesList.append(rule)
		return rulesList

	def convertQuestion(questionCondition):
		question=''
		evenItems=list(np.random.choice(evenList,questionCondition.count('even'),replace=False))
		oddItems=list(np.random.choice(oddList,questionCondition.count('odd'),replace=False))
		vowelsItems=list(np.random.choice(vowelsList,questionCondition.count('vowels'),replace=False))
		consonantsItems=list(np.random.choice(consonantsList,questionCondition.count('consonants'),replace=False))
		tempList=[x for x in letterList if x not in evenItems+oddItems+vowelsItems+consonantsItems]
		letterItems=list(np.random.choice(tempList,questionCondition.count('letter'),replace=False))

		for condition in questionCondition:
			if condition=='even':
				question+=evenItems.pop()
			elif condition=='odd':
				question+=oddItems.pop()
			elif condition=='vowels':
				question+=vowelsItems.pop()
			elif condition=='consonants':
				question+=consonantsItems.pop()
			else:
				question+=letterItems.pop()

		return question

	def createSolutionRule(rulesList):
		symbols=[]
		for key in representationList:
			symbols.append(representationList[key])
		solutionRule=list(np.random.choice(['interchange',random.choice(symbols),'first_as_last','last_as_first'],3,replace=False))
		for i in range(len(solutionRule)):
			rulesList[i].append(solutionRule.pop())
		return rulesList

	def decodeExpression(exp,rule):
		decodedExpression=[]
		for letter in exp:
			decodedExpression.insert(len(decodedExpression),representationList[letter])
		if rule[4]=='interchange':
			swap=decodedExpression[rule[0]-1]
			decodedExpression[rule[0]-1]=decodedExpression[rule[1]-1]
			decodedExpression[rule[1]-1]=swap
		elif rule[4]=='first_as_last':
			decodedExpression[rule[0]-1]=decodedExpression[rule[1]-1]
		elif rule[4]=='last_as_first':
			decodedExpression[rule[1]-1]=decodedExpression[rule[0]-1]
		else:
			decodedExpression[rule[0]-1]=rule[4]
			decodedExpression[rule[1]-1]=rule[4]
		return ''.join(decodedExpression)

	def createSolution(questionList,rulesList,questionType):
		solutionList=[]
		for i in range(4):
			solutionList.append(decodeExpression(questionList[i],rulesList[questionType[i]-1]))
		lastExp=''
		for letter in questionList[4]:
			lastExp+=representationList[letter]

		solutionList.append(lastExp)

		return solutionList

	def createOptions(solution):
		def createOption(exp):
			symbols=[]
			for key in representationList:
				symbols.append(representationList[key])
			indexList=list(np.random.choice([0,1,2,3,4,5],2))
			exp=list(exp)
			exp[indexList[0]]=random.choice(symbols)
			exp[indexList[1]]=random.choice(symbols)
			return ''.join(exp)

		optionsList=[solution]
		while len(optionsList)<4:
			option=createOption(solution)
			if option not in optionsList:
				optionsList.append(option)
		optionsList.append('None of these')
		return optionsList


	def checkNoRule(noRuleQuestion,rulesList):
		status=False
		itemDict={}
		itemDict['even']=evenList
		itemDict['odd']=oddList
		itemDict['vowels']=vowelsList
		itemDict['consonants']=consonantsList

		for item in rulesList:
			if noRuleQuestion[item[0]-1] in itemDict[item[2]] and noRuleQuestion[item[1]-1] in itemDict[item[3]]:
				status=True
				break

		return status

	def createQuestion(rulesList,representationList):
		global vowelsList,consonantsList,evenList,oddList,letterList
		vowelsList=[]
		consonantsList=[]
		evenList=[]
		oddList=[]
		letterList=[]
		for key in representationList:
			letterList.append(key)
			if key in vowels:
				vowelsList.append(key)
			elif key in consonants:
				consonantsList.append(key)
			elif key in even:
				evenList.append(key)
			elif key in odd:
				oddList.append(key)
			else:
				pass

		questionList=[]
		questionConditionList=[]
		questionType=[]
		indexList=[0,1,2]
		indexList.append(random.choice([0,1,2]))
		while len(questionList)<4:
			index=indexList.pop()
			rule=rulesList[index]
			questionType.append(index+1)
			questionCondition=['letter' for i in range(6)]
			questionCondition[rule[0]-1]=rule[2]
			questionCondition[rule[1]-1]=rule[3]
			questionConditionList.append(questionCondition)
			questionList.append(convertQuestion(questionCondition))
		questionCondition=list(np.random.choice(['letter','even','odd','vowels','consonants'],6))
		noRuleQuestion=convertQuestion(questionCondition)
		while checkNoRule(noRuleQuestion,rulesList):
			questionCondition=list(np.random.choice(['letter','even','odd','vowels','consonants'],6))
			noRuleQuestion=convertQuestion(questionCondition)
		questionList.append(convertQuestion(questionCondition))
		questionType.append(0)
		return questionList,questionType

	def createText(rulesList,questionList,questionType,optionsMainList):
		textHelperDict={1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth','consonants':'consonant','vowels':'vowel','even':'even','odd':'odd'}
		text='Consider the following data:\n'
		for key in representationList:
			text+=str(key)+' - '+str(representationList[key])+'\n'
		text+='\nEach element is denoted by a symbol as shown above. Further, consider the given conditions and answer accordingly.\n'
		count=1
		for rule in rulesList:
			if rule[4]=='interchange':
				text+='({}) If the {} letter of the word is {} and {} letter is {}, then the code for both the letters should be interchanged.\n'.format(count,textHelperDict[rule[0]],textHelperDict[rule[2]],textHelperDict[rule[1]],textHelperDict[rule[3]])
			elif rule[4]=='first_as_last':
				text+='({}) If the {} letter of the word is {} and {} letter is {}, then the code for {} letter should be the code for {} letter.\n'.format(count,textHelperDict[rule[0]],textHelperDict[rule[2]],textHelperDict[rule[1]],textHelperDict[rule[3]],textHelperDict[rule[0]],textHelperDict[rule[1]])
			elif rule[4]=='last_as_first':
				text+='({}) If the {} letter of the word is {} and {} letter is {}, then the code for {} letter should be the code for {} letter.\n'.format(count,textHelperDict[rule[0]],textHelperDict[rule[2]],textHelperDict[rule[1]],textHelperDict[rule[3]],textHelperDict[rule[1]],textHelperDict[rule[0]])
			else:
				text+='({}) If the {} letter of the word is {} and {} letter is {}, then the code for both the letters should be coded as \'{}\'.\n'.format(count,textHelperDict[rule[0]],textHelperDict[rule[2]],textHelperDict[rule[1]],textHelperDict[rule[3]],rule[4])
			count+=1

		indexList=list(np.random.choice([0,1,2,3,4],5,replace=False))
		count=1
		for index in indexList:
			text+='\n\n{}. {}\n'.format(count,questionList[index])
			options=optionsMainList[index]
			answer=random.choice([0,1,2,3])
			swap=options[answer]
			options[answer]=options[0]
			options[0]=swap
			text+='(1) {}\n(2) {}\n(3) {}\n(4) {}\n(5) {}\nAnswer key : {}\n'.format(options[0],options[1],options[2],options[3],options[4],answer+1)
			if questionType[index]==0:
				text+='Solution: It follows no rule.\n\n'
			else:
				text+='Solution: By rule ({})\n'.format(questionType[index])
			count+=1

		return text



	representationList=createRepresentation()
	rulesList=createRules()
	questionList,questionType=createQuestion(rulesList,representationList)
	createSolutionRule(rulesList)
	solutions=createSolution(questionList,rulesList,questionType)
	optionsMainList=[]
	for solution in solutions:
		optionsMainList.append(createOptions(solution))
	text=createText(rulesList,questionList,questionType,optionsMainList)
	return text

countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	try:
		text=str('\nSet {}\n\n').format(sets_count+1)+main()
		#print "Set {}".format(i+1)
		global fn
		fn = os.path.join(os.path.dirname(__file__), 'sampleQuestions.txt')
		file = open(fn, "a")
	 	file.write(text)
	 	file.close()
	 	sets_count+=1
	except:
		print ('\n')+"Error in Set {}".format(sets_count+1)
		pass
print 'Done. Output written to file : {} '.format(fn)