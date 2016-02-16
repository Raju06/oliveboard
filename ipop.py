def execute():# type 1 - vowels_descending + consonants_ascending 
	alist=raw_input("Enter the list with equal spacing in between words \n") .split()
	print ("Enter serial no. of type of question you wish to check from following list")
	input_type = raw_input("Type - 1 : vowels_ascending + consonants_ascending\nType - 2 : vowels_ascending + consonants_descending\nType - 3 : vowels_descending + consonants_ascending\nType - 4 : vowels_descending + consonants_descending\nType - 5 : consonants_ascending + vowels_ascending\nType - 6 : consonants_ascending + vowels_descending\nType - 7 : consonants_descending + vowels_ascending\nType - 8 : consonants_descending + vowels_descending\n")
	alist_length=len(alist)
	alist_vowels=[]
	alist_vowel_words=[]
	alist_vowels_rank=[]
	alist_vowels_order=[]
	alist_consonants=[]
	alist_consonant_words=[]
	alist_consonants_rank=[]
	alist_consonants_order=[]
	alist_vowels_order=[]

	vowels=['a','e','i','o','u']
	consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

	def arrange(blist,item,num):
		found = False
		i=0
		while not found:
			if item==blist[i]:
				blist.insert(num,blist.pop(i))
				found = True
			i+=1
		return blist


	def status(alist):
		for i in range(alist_length):
			if (alist[i][0] in vowels):
				alist_vowels.append(alist[i][0])
				alist_vowels_order.append(i)
				alist_vowels_rank.append(26+(ord(alist[i][0])))
				alist_vowel_words.append(alist[i])
			else:
				alist_consonants.append(alist[i][0])
				alist_consonants_order.append(i)
				alist_consonants_rank.append(ord((alist[i][0])))
				alist_consonant_words.append(alist[i])


	status(alist)

	def checksorted(rlist,input_type,alist_vowels):
		alist=[]
		for i in range(len(rlist)):
			alist.append(rlist[i][0])
		#print alist
		#print alist_vowels	
		class createList():
			def __init__(self,alist,input_type,alist_vowels):
				self.alist=alist
				self.input_type=input_type
				self.vowels_count=len(alist_vowels)
				if self.input_type in ['1','2','3','4']: #vowels are to the left
					self.vowels_list=(self.alist[0:self.vowels_count])
					self.consonants_list=(self.alist[self.vowels_count:len(self.alist)])
				else:#vowels are to the right
					self.vowels_list=(self.alist[len(self.alist)-self.vowels_count:len(self.alist)])
					self.consonants_list=(self.alist[0:len(self.alist)-self.vowels_count])

		newlist=createList(alist,input_type,alist_vowels)

		def isVowelList(blist):
			op=1
			i=0
			while i < len(blist) and op==1:
				if blist[i] not in ['a','e','i','o','u']:
					op=0
				
				i+=1
			if op==1:
				return 1
			else:
				return 0


		def checkAscending(blist):
			op=1
			i=0
			while i < len(blist)-1 and op==1:
				if ord(blist[i])>ord(blist[i+1]):
					op=0
				
				i+=1
			if op==1:
				return 1
			else:
				return 0

		def checkDescending(blist):
			op=1
			i=0
			while i < len(blist)-1 and op==1:
				if ord(blist[i])<ord(blist[i+1]):
					op=0
				
				i+=1
			if op==1:
				return 1
			else:
				return 0

		#print "vowelslist",newlist.vowels_list
		
		if isVowelList(newlist.vowels_list):
			
			if input_type == '1':
				return checkAscending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
			elif input_type == '2':
				return checkAscending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
			elif input_type == '3':
				return checkDescending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
			elif input_type == '4':
				return checkDescending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
			elif input_type == '5':
				return checkAscending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
			elif input_type == '6':
				return checkDescending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
			elif input_type == '7':
				return checkAscending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
			else:	
				return checkDescending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
		else:
			return 0

	#print checksorted(alist,input_type,alist_vowels)
	#print alist_vowels
	#print alist


	finalList=[]
	if input_type=='1':
		j=0
		k=len(alist)-1
		
		while checksorted(alist,input_type,alist_vowels)!=1:
			if j<len(alist_vowels):
				
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(min(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(min(alist_vowels_rank))]=300
				j+=1
			if k>=len(alist_vowels):

				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(max(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(max(alist_consonants_rank))]=0
				k-=1
			
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='2':
		j=0
		k=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j<len(alist_vowels):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(min(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(min(alist_vowels_rank))]=300
				j+=1
			if k>=len(alist_vowels):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(min(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(min(alist_consonants_rank))]=300
				k-=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='3':
		j=0
		k=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j<len(alist_vowels):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(max(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(max(alist_vowels_rank))]=0
				j+=1
			if k>=len(alist_vowels):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(max(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(max(alist_consonants_rank))]=0
				k-=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='4':
		j=0
		k=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j<len(alist_vowels):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(max(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(max(alist_vowels_rank))]=0
				j+=1
			if k>=len(alist_vowels):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(min(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(min(alist_consonants_rank))]=300
				k-=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='5':
		k=0
		j=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j>=len(alist_consonants):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(max(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(max(alist_vowels_rank))]=0
				j-=1
			if k<len(alist_consonants):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(min(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(min(alist_consonants_rank))]=300
				k+=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='6':
		k=0
		j=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j>=len(alist_consonants):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(min(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(min(alist_vowels_rank))]=300
				j-=1
			if k<len(alist_consonants):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(min(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(min(alist_consonants_rank))]=300
				k+=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	elif input_type=='7':
		k=0
		j=len(alist)-1

		while checksorted(alist,input_type,alist_vowels)!=1:
			if j>=len(alist_consonants):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(max(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(max(alist_vowels_rank))]=0
				j-=1
			if k<len(alist_consonants):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(max(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(max(alist_consonants_rank))]=0
				k+=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
	else:	

		k=0
		j=len(alist)-1
		while checksorted(alist,input_type,alist_vowels)!=1:
			if j>=len(alist_consonants):
				high_rank_vowels=alist_vowel_words[alist_vowels_rank.index(min(alist_vowels_rank))]
				arrange(alist,high_rank_vowels,j)
				alist_vowels_rank[alist_vowels_rank.index(min(alist_vowels_rank))]=300
				j-=1
			if k<len(alist_consonants):
				high_rank_consonants=alist_consonant_words[alist_consonants_rank.index(max(alist_consonants_rank))]
				arrange(alist,high_rank_consonants,k)
				alist_consonants_rank[alist_consonants_rank.index(max(alist_consonants_rank))]=0
				k+=1
			finalList.append(" ".join(alist))
			print " ".join(alist)
		#print "alist is" ,alist
		#print checksorted(alist)
	return finalList		

finalList=execute()

done=1
while done!='0':
	raw_input("Press enter to continue....")
	print ("Enter type of the question from following list ")
	question_type=raw_input("Type 1 : How many steps are required to sort it?\nType 2 : What is step X?\nType 3 : In which step do we get following order?\nType 4 : In step X, what is Yth element from left/right\nType 5 : what is position of element X in step Y\nType 6 : In step X what are the number of words between A and B?\nType 0 if you want to exit \n")
	done=question_type
	if question_type=='1':
		print "Number of steps required to sort is : ",len(finalList)
	elif question_type=='2':
		step=int(raw_input("Enter the step no. : "))
		print "Step {} is : \n".format(step),finalList[step-1]
	elif question_type=='3':
		order1=raw_input("Enter the order without any quotes ")
		print "In step - {} we get above order : ".format(finalList.index(order1)+1)
	elif question_type=='4':
		X=int(raw_input("Enter step no."))
		Y=int(raw_input("Enter the position no. of the element wrt left/right "))
		gh=raw_input("Postion is from left or right?(Enter all in small caps) ")
		listelement=finalList[X-1].split()
		#print listelement
		if gh=='left':
			print "Element in step - {} at postion - {} from {} is : {}".format(X,Y,gh,listelement[Y-1])
		else:
			print "Element in step - {} at postion - {} from {} is : {}".format(X,Y,gh,listelement[len(listelement)-Y])
	elif question_type=='5':
		X=int(raw_input("Enter step no."))
		gh=raw_input("What is the element?(Enter all in small caps")
		listelement=finalList[X-1].split()
		for i in range(len(listelement)):
			if listelement[i]==gh:
				ph=i+1
				break
		print "Element is at position - {} in step - {}".format(ph,X)
	elif question_type=='6':
		X=int(raw_input("Enter step no."))
		gh=raw_input("What is the first element?(Enter all in small caps)")
		fh=raw_input("What is the second element?(Enter all in small caps)")
		listelement=finalList[X-1].split()
		value=abs(listelement.index(gh)-listelement.index(fh))
		print "There are {} words between {} and {} in step - {}".format(value,gh,fh,X)
	else:
		if question_type!='0':
			print "error in input"
		