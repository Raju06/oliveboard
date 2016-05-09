import random,os
import numpy as np
import itertools
def main(level_of_difficulty):
	def shuffle(x):
	    x = list(x)
	    random.shuffle(x)
	    return x

	def indices(lst, element):
	    result = []
	    offset = -1
	    while True:
	        try:
	            offset = lst.index(element, offset+1)
	        except ValueError:
	        	return result
	        result.append(offset)

	def createDifficultylevel(level_of_difficulty):
		if level_of_difficulty==1:
			number_of_lines=4
			number_of_words=random.randrange(8,11)
		elif level_of_difficulty==2:
			number_of_lines=4
			number_of_words=random.randrange(11,13)
		elif level_of_difficulty==3:
			number_of_lines=5
			number_of_words=random.randrange(13,16)
		else:
			pass
		return number_of_lines,number_of_words

	def createList(number_of_lines,number_of_words):
		list_individual_length=list(np.random.choice([1,2,3],number_of_words,p=[0.3,0.5,0.2]))
		count=0
		for i in range(len(list_individual_length)):
			count+=list_individual_length[i]
		if number_of_lines**2>count:	
			sets_source=[number_of_lines*[i] for i in range(1,number_of_lines+1)]
			#print sets_source
			sets_list=[]
			for i in range(number_of_words):
				sets_list.append([])

			for i in range(number_of_words):
				for j in range(list_individual_length[i]):
					appended=False
					while not appended:	
						k=random.randrange(1,number_of_lines+1)
						if len(sets_source[k-1])!=0:
							if sets_source[k-1][0] not in sets_list[i]:
								sets_list[i].append(sets_source[k-1].pop())
								appended=True
			for sublist in sets_list:
				sublist.sort()
			return sets_list
		else:
			return 0
		
	def createLeftlist(left_list):
		fh=open("C:\Users\Olive\Desktop\oliveboard\project_language\samplewords.txt", "r")
		for line in fh:
			samplewords=line.split()
		words_list=[]
		while len(words_list)<len(left_list):
			item_index=random.randrange(0,len(samplewords))
			if len(str(samplewords[item_index]))<6 and samplewords[item_index] not in words_list:
				#print "Hola"
				words_list.append(samplewords[item_index])
		return words_list

	def createRightlist(right_list):
		return list(np.random.choice([i for i in range(10,100)],len(right_list),replace=False))

	def createLineslist(items_list,alist,number_of_lines):
		lines_list=[]
		for i in range(number_of_lines):
			lines_list.append([])
		for i in range(len(alist)):
			for j in range(len(alist[i])):
				lines_list[alist[i][j]-1].append(items_list[i])
		return lines_list

	def outputList(left_list,right_list):
		left_helper_list=[]
		right_helper_list=[]
		unique_left_list=[]
		for i in range(len(left_list)):
			if left_list[i]not in unique_left_list:
				left_helper_list.append(indices(left_list,left_list[i]))
				right_helper_list.append(indices(right_list,left_list[i]))
				unique_left_list.append(left_list[i])
		return left_helper_list,right_helper_list

	def findLink(fromList,toList,item):
		for i in range(len(fromList)):
			for j in range(len(fromList[i])):
				if fromList[i][j]==item:
					if len(fromList[i])==1:
						return [toList[i][j]]
					else:
						return toList[i]	

	def generateQuestions(left_items_list,right_items_list,left_output_items_list,right_output_items_list):
		questionlist=[]
		optionlist=[]
		number_of_questions=0
		question_type_list=list(np.random.choice(['1','2','3','4','5','6'],5,replace=False))
		for i in range(5):
			questionType=question_type_list.pop()
			if questionType=='1':
				def noAnswerOption(questionItem,right_items_list):
					k=[]
					while len(k)<3:
						temp=list(np.random.choice(right_items_list,len(questionItem),replace=False))
						if temp not in k:
							k.append(temp)
					return k

				#print "left items list is ",left_items_list
				questionItem=list(np.random.choice(left_items_list,random.randrange(2,4),replace=False))
				answerItemList=[]
				for j in range(len(questionItem)):
					answerItemList.append(findLink(left_output_items_list,right_output_items_list,questionItem[j]))
				answerItem=list(itertools.product(*answerItemList))
				for i in range(len(answerItem)):
					answerItem[i]=list(answerItem[i])
					templist=list(itertools.permutations(answerItem[i],len(answerItem[i])))
					for j in range(len(templist)):
						if list(templist[j]) not in answerItem:
							answerItem.append(list(templist[j]))

				answerItemTemp=[]
				for i in range(len(answerItem)):
					if len(set(answerItem[i]))==len(answerItem[i]):
						answerItemTemp.append(answerItem[i])
				answerItem=answerItemTemp
				
				optionlist1=noAnswerOption(questionItem,right_items_list)
				done=False
				stop=False
				while not done:		
					for k in range(len(optionlist1)):
						if optionlist1[k] in answerItem:
							break
							stop=True
					if stop:
						optionlist1=noAnswerOption(questionItem,right_items_list)
					else:
						options=shuffle([answerItem[random.randrange(0,len(answerItem))],optionlist1[0],optionlist1[1],optionlist1[2]])
						done=True
				if type(questionItem)==list:
					questionItem=' '.join(str(e) for e in questionItem)
				questionlist.append("How can '{}' be coded?".format(questionItem))
				options.append(["None of the above"])
				for i in range(len(options)):
					if options[i] in answerItem:
						options.append(str(i+1))
						break						
				optionlist.append(options)
			if questionType=='2':
				questionItem=[left_items_list[random.randrange(0,len(left_items_list))]]
				answerItem=[]
				for j in range(len(questionItem)):
					answerItem.append(findLink(left_output_items_list,right_output_items_list,questionItem[j]))
				answerItem=answerItem[0]
				right_items_list_temp=[]
				for i in range(len(right_items_list)):
					if right_items_list[i] not in answerItem:
						right_items_list_temp.append(right_items_list[i])
				optionlist1=list(np.random.choice(right_items_list_temp,4,replace=False))
				#print questionItem
				#print answerItem
				#print optionlist1
				options=shuffle([answerItem[random.randrange(0,len(answerItem))],optionlist1[0],optionlist1[1],optionlist1[2],optionlist1[3]])
				if type(questionItem)==list:
					questionItem=' '.join(str(e) for e in questionItem)
				questionlist.append("What is the code for '{}' ?".format(questionItem))
				for i in range(len(options)):
					if options[i] in answerItem:
						options.append(str(i+1))
						break
				optionlist.append(options)
			if questionType=='3':
				questionItem=[right_items_list[random.randrange(0,len(right_items_list))]]
				answerItem=[]
				for j in range(len(questionItem)):
					answerItem.append(findLink(right_output_items_list,left_output_items_list,questionItem[j]))
				answerItem=answerItem[0]
				left_items_list_temp=[]
				for i in range(len(left_items_list)):
					if left_items_list[i] not in answerItem:
						left_items_list_temp.append(left_items_list[i])
				optionlist1=list(np.random.choice(left_items_list_temp,4,replace=False))
				#print questionItem
				#print answerItem
				#print optionlist1
				options=shuffle([answerItem[random.randrange(0,len(answerItem))],optionlist1[0],optionlist1[1],optionlist1[2],optionlist1[3]])
				if type(questionItem)==list:
					questionItem=' '.join(str(e) for e in questionItem)
				questionlist.append("Which word is coded as '{}' ?".format(questionItem))
				for i in range(len(options)):
					if options[i] in answerItem:
						options.append(str(i+1))
						break
				optionlist.append(options)
			if questionType=='4':
				count=0
				for i in range(len(right_output_list)):
					if len(right_output_list[i])==1:
						count+=1
				answerItem=count
				options=shuffle([answerItem,answerItem-3,answerItem-1,answerItem-4,answerItem-2])
				questionlist.append("For how many distinct words can their respective codes be determined?")
				options.append(str(options.index(answerItem)+1))
				optionlist.append(options)
			if questionType=='5':
				def noAnswerOption(questionItem,right_items_list):
					k=[]
					while len(k)<3:
						temp=list(np.random.choice(right_items_list,len(questionItem),replace=False))
						if temp not in k:
							k.append(temp)
					return k

				#print "left items list is ",left_items_list
				questionItem=list(np.random.choice(left_items_list,random.randrange(3,4),replace=False))
				answerItemList=[]
				for j in range(len(questionItem)):
					answerItemList.append(findLink(left_output_items_list,right_output_items_list,questionItem[j]))
				answerItem=list(itertools.product(*answerItemList))
				answerItemTemp=[]
				for i in range(len(answerItem)):
					if len(set(answerItem[i]))==len(answerItem[i]):
						answerItemTemp.append(answerItem[i])
				answerItem=answerItemTemp
				for i in range(len(answerItem)):
					answerItem[i]=list(answerItem[i])
					templist=list(itertools.permutations(answerItem[i],len(answerItem[i])))
					for j in range(len(templist)):
						if list(templist[j]) not in answerItem:
							answerItem.append(list(templist[j]))
				optionlist1=noAnswerOption(questionItem,right_items_list)
				appended=False
				while not appended:
					newItem="".join(createLeftlist([1]))
					if newItem not in questionItem:
						removedItem=questionItem[len(questionItem)-1]
						questionItem[len(questionItem)-1]=newItem
						appended=True
				done=False
				stop=False
				while not done:		
					for k in range(len(optionlist1)):
						if optionlist1[k] in answerItem:
							break
							stop=True
					if stop:
						optionlist1=noAnswerOption(questionItem,right_items_list)
					else:
						newAnswerItemList=[]
						newQuestionItem=questionItem[:len(questionItem)-1]
						for j in range(len(newQuestionItem)):
							newAnswerItemList.append(findLink(left_output_items_list,right_output_items_list,newQuestionItem[j]))
						newAnswerItem=list(itertools.product(*newAnswerItemList))
						newAnswerItemTemp=[]
						for i in range(len(newAnswerItem)):
							if len(set(newAnswerItem[i]))==len(newAnswerItem[i]):
								newAnswerItemTemp.append(newAnswerItem[i])
						newAnswerItem=newAnswerItemTemp
						
						appended1=False
						while not appended1:
							newOption=random.randrange(10,100)
							if newOption not in right_items_list:
								newOptionItem=list(newAnswerItem[0])+[newOption]
								appended1=True

						options=shuffle([newOptionItem,optionlist1[0],optionlist1[1],optionlist1[2]])
						done=True
				if type(questionItem)==list:
					questionItem=' '.join(str(e) for e in questionItem)
				questionlist.append("How can '{}' be coded?".format(questionItem))
				options.append(["None of the above"])
				options.append(str(options.index(newOptionItem)+1))
				optionlist.append(options)
			if questionType=='6':
				def noAnswerOption(questionItem,left_items_list):
					k=[]
					while len(k)<3:
						temp=list(np.random.choice(left_items_list,len(questionItem),replace=False))
						if temp not in k:
							k.append(temp)
					return k

				#print "left items list is ",left_items_list
				questionItem=list(np.random.choice(right_items_list,random.randrange(2,4),replace=False))
				answerItemList=[]
				for j in range(len(questionItem)):
					answerItemList.append(findLink(right_output_items_list,left_output_items_list,questionItem[j]))
				answerItem=list(itertools.product(*answerItemList))
				for i in range(len(answerItem)):
					answerItem[i]=list(answerItem[i])
					templist=list(itertools.permutations(answerItem[i],len(answerItem[i])))
					for j in range(len(templist)):
						if list(templist[j]) not in answerItem:
							answerItem.append(list(templist[j]))

				answerItemTemp=[]
				for i in range(len(answerItem)):
					if len(set(answerItem[i]))==len(answerItem[i]):
						answerItemTemp.append(answerItem[i])
				answerItem=answerItemTemp
				
				optionlist1=noAnswerOption(questionItem,left_items_list)
				done=False
				stop=False
				while not done:		
					for k in range(len(optionlist1)):
						if optionlist1[k] in answerItem:
							break
							stop=True
					if stop:
						optionlist1=noAnswerOption(questionItem,left_items_list)
					else:
						options=[answerItem[random.randrange(0,len(answerItem))],optionlist1[0],optionlist1[1],optionlist1[2]]
						done=True
				if type(questionItem)==list:
					questionItem=' '.join(str(e) for e in questionItem)
				questionlist.append("Which of the following can be coded as '{}' ?".format(questionItem))
				options=shuffle(options)
				options.append(["None of the above"])
				for i in range(len(options)):
					if options[i] in answerItem:
						options.append(str(i+1))
						break
				optionlist.append(options)
		local_text=""
		for i in range(len(questionlist)):
			for j in range(5):
				if type(optionlist[i][j])==list:
					optionlist[i][j]=' '.join(str(e) for e in optionlist[i][j])
			local_text+= "\n{}.{}\n(1){}\n(2){}\n(3){}\n(4){}\n(5){}\nAnswer key:{}\n".format(i+1,questionlist[i],optionlist[i][0],optionlist[i][1],optionlist[i][2],optionlist[i][3],optionlist[i][4],optionlist[i][5])
		return local_text


	#level_of_difficulty=input('Enter level of difficulty')
	text=''
	number_of_lines,number_of_words=createDifficultylevel(level_of_difficulty)
	output=0
	while output==0:
		output=createList(number_of_lines,number_of_words)
		#print "Hola"
	sets_list=output
	global left_list
	#print sets_list
	left_list=sets_list
	right_list=shuffle(sets_list)
	global left_lines_list
	left_items_list=createLeftlist(left_list)
	right_items_list=createRightlist(right_list)
	left_lines_list=createLineslist(left_items_list,left_list,number_of_lines)
	right_lines_list=createLineslist(right_items_list,right_list,number_of_lines)
	left_output_list,right_output_list=outputList(left_list,right_list)
	
	list1=[]
	list2=[]
	text+='In a certain code language \n'
	for i in range(len(left_lines_list)):
		list1.append(' '.join(list(shuffle(left_lines_list[i]))))
		list2.append(' '.join(str(x) for x in list(shuffle(right_lines_list[i]))))
	for i in range(len(left_lines_list)):
		text+="\'{}\' is written as \'{}\'\n".format(list1[i],list2[i])
	
	left_output_items_list=[]
	right_output_items_list=[]
	resultList=[]
	for i in range(len(left_output_list)):
		left_item=[]
		right_item=[]
		left_output_items_list.append([])
		right_output_items_list.append([])
		for j in range(len(left_output_list[i])):
			left_output_items_list[i].append(left_items_list[left_output_list[i][j]])
			right_output_items_list[i].append(right_items_list[right_output_list[i][j]])	
			left_item.append(str(left_items_list[left_output_list[i][j]]))
			right_item.append(str(right_items_list[right_output_list[i][j]]))
		resultList.append([left_item,right_item])
	
	solutiontext='Common solution: \n\n'
	for i in range(len(left_lines_list)):
		solutiontext+="\'{}\' is written as \'{}\'---------------({})\n".format(list1[i],list2[i],i+1)

	resultList2=[]
	for i in range(len(left_list)):
		itemName=left_items_list[i]
		for j in range(len(resultList)):
			for k in range(len(resultList[j])):
				for m in range(len(resultList[j][k])):
					if resultList[j][k][m]==itemName:
						indexName=j
						break
		resultList2.append([left_list[i],itemName,resultList[indexName][1]])

	text1,text2,text3,text4='','','',''
	for i in range(len(resultList2)):
		if len(resultList2[i][0])==4:
			text4+='From {}: {} is {}\n'.format(','.join(str(x) for x in resultList2[i][0]),resultList2[i][1],'/'.join(resultList2[i][2]))
		elif len(resultList2[i][0])==3:
			text3+='From {}: {} is {}\n'.format(','.join(str(x) for x in resultList2[i][0]),resultList2[i][1],'/'.join(resultList2[i][2]))
		elif len(resultList2[i][0])==2:
			text2+='From {}: {} is {}\n'.format(','.join(str(x) for x in resultList2[i][0]),resultList2[i][1],'/'.join(resultList2[i][2]))
		elif len(resultList2[i][0])==1:
			text1+='From {}: By elimination, {} is {}\n'.format(','.join(str(x) for x in resultList2[i][0]),resultList2[i][1],'/'.join(resultList2[i][2]))
		else:
			print "Error"	

	solutiontext+='\n'+text4+text3+text2+text1+'\n'+'Summary:\n'

	left_output_items_list=[]
	right_output_items_list=[]

	for i in range(len(left_output_list)):
		left_item=''
		right_item=''
		left_output_items_list.append([])
		right_output_items_list.append([])
		for j in range(len(left_output_list[i])):
			left_output_items_list[i].append(left_items_list[left_output_list[i][j]])
			right_output_items_list[i].append(right_items_list[right_output_list[i][j]])	
			left_item+=str(left_items_list[left_output_list[i][j]])+str('/')
			right_item+=str(right_items_list[right_output_list[i][j]])+str('/')


		solutiontext+= "{} is {}\n".format(left_item[:len(left_item)-1],right_item[:len(right_item)-1])

	text+=generateQuestions(left_items_list,right_items_list,left_output_items_list,right_output_items_list)
	text+=str('\n\n')+solutiontext
	return text

countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	try:
		level_of_difficulty=random.randrange(1,4)
		text=str('\nSet {}\n\n').format(sets_count+1)+main(level_of_difficulty)
		#print "Set {}".format(i+1)
		criteria_met=True
		for i in range(len(left_lines_list)):
			if len(left_lines_list[i])<3:
				criteria_met=False
				break
		if criteria_met:
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