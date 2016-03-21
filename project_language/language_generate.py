import random
import numpy as np

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
		number_of_words=random.randrange(7,10)
	elif level_of_difficulty==2:
		number_of_lines=5
		number_of_words=random.randrange(9,12)
	elif level_of_difficulty==3:
		number_of_lines=6
		number_of_words=random.randrange(11,14)
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
		if len(str(samplewords[item_index]))<6:
			#print "Hola"
			words_list.append(samplewords[item_index])
	return words_list

def createRightlist(right_list):
	return list(np.random.choice([i for i in range(10,100)],len(right_list),replace=False))

def createLineslist(items_list,list,number_of_lines):
	lines_list=[]
	for i in range(number_of_lines):
		lines_list.append([])
	for i in range(len(list)):
		for j in range(len(list[i])):
			lines_list[list[i][j]-1].append(items_list[i])
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


level_of_difficulty=input('Enter level of difficulty')
number_of_lines,number_of_words=createDifficultylevel(level_of_difficulty)
output=0
while output==0:
	output=createList(number_of_lines,number_of_words)
	#print "Hola"
sets_list=output

#print sets_list
left_list=sets_list
right_list=shuffle(sets_list)

left_items_list=createLeftlist(left_list)
right_items_list=createRightlist(right_list)
left_lines_list=createLineslist(left_items_list,left_list,number_of_lines)
right_lines_list=createLineslist(right_items_list,right_list,number_of_lines)
left_output_list,right_output_list=outputList(left_list,right_list)


for i in range(len(left_lines_list)):
	print "{} is {}\n".format(shuffle(left_lines_list[i]),shuffle(right_lines_list[i]))

for i in range(len(left_output_list)):
	left_item=''
	right_item=''
	for j in range(len(left_output_list[i])):
		left_item+=str(left_items_list[left_output_list[i][j]])+str('/')
		right_item+=str(right_items_list[right_output_list[i][j]])+str('/')

	print "{} is {}".format(left_item[:len(left_item)-1],right_item[:len(right_item)-1])



