def checkSorted(alist,input_value,alist_vowels):
	class createList():
		def __init__(self,alist,input_value,alist_vowels):
			self.alist=alist
			self.input_value=input_value
			self.vowels_count=len(alist_vowels)
			if self.input_value in ['1','2','3','4']: #vowels are to the left
				self.vowels_list=(self.alist[0:self.vowels_count])
				self.consonants_list=(self.alist[self.vowels_count:len(self.alist)])
			else:#vowels are to the right
				self.vowels_list=(self.alist[len(self.alist)-self.vowels_count:len(self.alist)])
				self.consonants_list=(self.alist[0:len(self.alist)-self.vowels_count])

	newlist=createList(alist,input_value,alist_vowels)			
	def isVowelList(blist):
		op=1
		i=0
		while i < len(blist)-1 and op==1:
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
		#print "inside if"
		if input_value == '1':
			return checkAscending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
		elif input_value == '2':
			return checkAscending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
		elif input_value == '3':
			return checkDescending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
		elif input_value == '4':
			return checkDescending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
		elif input_value == '5':
			return checkAscending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
		elif input_value == '6':
			return checkDescending(newlist.vowels_list) and checkAscending(newlist.consonants_list)
		elif input_value == '7':
			return checkAscending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
		else:	
			return checkDescending(newlist.vowels_list) and checkDescending(newlist.consonants_list)
	else:
		return 0

alist=raw_input("enter list")
input_value=raw_input("input value")
alist_vowels=['a','e']
print checkSorted(alist,input_value,alist_vowels)

