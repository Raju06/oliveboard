# type 1 - vowels_descending + consonants_ascending 
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
		print " ".join(alist)
	#print "alist is" ,alist
	#print checksorted(alist)