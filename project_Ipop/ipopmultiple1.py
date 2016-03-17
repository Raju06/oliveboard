#defined functions
from __future__ import division
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                       ZeroOrMore,Forward,nums,alphas,oneOf)
import operator
import random
import math
import numpy as np
from sets import Set

def mainFunction():
	global final_output
	final_output=[]
	
	class NumericStringParser(object):
	    '''
	    Most of this code comes from the fourFn.py pyparsing example
	    '''
	    def pushFirst(self, strg, loc, toks ):
	        self.exprStack.append( toks[0] )
	    def pushUMinus(self, strg, loc, toks ):
	        if toks and toks[0]=='-': 
	            self.exprStack.append( 'unary -' )
	    def __init__(self):
	        """
	        expop   :: '^'
	        multop  :: '*' | '/'
	        addop   :: '+' | '-'
	        integer :: ['+' | '-'] '0'..'9'+
	        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
	        factor  :: atom [ expop factor ]*
	        term    :: factor [ multop factor ]*
	        expr    :: term [ addop term ]*
	        """
	        point = Literal( "." )
	        e     = CaselessLiteral( "E" )
	        fnumber = Combine( Word( "+-"+nums, nums ) + 
	                           Optional( point + Optional( Word( nums ) ) ) +
	                           Optional( e + Word( "+-"+nums, nums ) ) )
	        ident = Word(alphas, alphas+nums+"_$")       
	        plus  = Literal( "+" )
	        minus = Literal( "-" )
	        mult  = Literal( "*" )
	        div   = Literal( "/" )
	        lpar  = Literal( "(" ).suppress()
	        rpar  = Literal( ")" ).suppress()
	        addop  = plus | minus
	        multop = mult | div
	        expop = Literal( "^" )
	        pi    = CaselessLiteral( "PI" )
	        expr = Forward()
	        atom = ((Optional(oneOf("- +")) +
	                 (pi|e|fnumber|ident+lpar+expr+rpar).setParseAction(self.pushFirst))
	                | Optional(oneOf("- +")) + Group(lpar+expr+rpar)
	                ).setParseAction(self.pushUMinus)       
	        # by defining exponentiation as "atom [ ^ factor ]..." instead of 
	        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
	        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
	        factor = Forward()
	        factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( self.pushFirst ) )
	        term = factor + ZeroOrMore( ( multop + factor ).setParseAction( self.pushFirst ) )
	        expr << term + ZeroOrMore( ( addop + term ).setParseAction( self.pushFirst ) )
	        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
	        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
	        # expr <<  general_term       
	        self.bnf = expr
	        # map operator symbols to corresponding arithmetic operations
	        epsilon = 1e-12
	        self.opn = { "+" : operator.add,
	                "-" : operator.sub,
	                "*" : operator.mul,
	                "/" : operator.truediv,
	                "^" : operator.pow }
	        self.fn  = { "sin" : math.sin,
	                "cos" : math.cos,
	                "tan" : math.tan,
	                "abs" : abs,
	                "trunc" : lambda a: int(a),
	                "round" : round,
	                "sgn" : lambda a: abs(a)>epsilon and cmp(a,0) or 0}
	    def evaluateStack(self, s ):
	        op = s.pop()
	        if op == 'unary -':
	            return -self.evaluateStack( s )
	        if op in "+-*/^":
	            op2 = self.evaluateStack( s )
	            op1 = self.evaluateStack( s )
	            return self.opn[op]( op1, op2 )
	        elif op == "PI":
	            return math.pi # 3.1415926535
	        elif op == "E":
	            return math.e  # 2.718281828
	        elif op in self.fn:
	            return self.fn[op]( self.evaluateStack( s ) )
	        elif op[0].isalpha():
	            return 0
	        else:
	            return float( op )
	    def eval(self,num_string,parseAll=True):
	        self.exprStack=[]
	        results=self.bnf.parseString(num_string,parseAll)
	        val=self.evaluateStack( self.exprStack[:] )
	        return val


	def quickSort(alist):
	   quickSortHelper(alist,0,len(alist)-1)

	def quickSortHelper(alist,first,last):
	   if first<last:

	       splitpoint = partition(alist,first,last)

	       quickSortHelper(alist,first,splitpoint-1)
	       quickSortHelper(alist,splitpoint+1,last)


	def partition(alist,first,last):
	   pivotvalue = alist[first]

	   leftmark = first+1
	   rightmark = last

	   done = False
	   while not done:

	       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
	           leftmark = leftmark + 1

	       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
	           rightmark = rightmark -1

	       if rightmark < leftmark:
	           done = True
	       else:
	           temp = alist[leftmark]
	           alist[leftmark] = alist[rightmark]
	           alist[rightmark] = temp

	   temp = alist[first]
	   alist[first] = alist[rightmark]
	   alist[rightmark] = temp
	   return rightmark

	def sortwords(a1,a2):
		x=min(len(a1),len(a2))
		ret=0
		for i in range(x):
			if ord(a1[i])>ord(a2[i]):
				ret=1
				break
			else:
				if ord(a1[i])<ord(a2[i]):
					ret=2
					break
		
		if ret==0:
			if len(a1)>=len(a2):
				ret= 1
			else:
				ret =2

		if ret==1:
			return 1
		else:
			return 0

	def bubbleSort(alist):
	    for passnum in range(len(alist)-1,0,-1):
	        for i in range(passnum):
	        		        	
	            if sortwords(alist[i],alist[i+1])==1:
	            	
	            	temp = alist[i]
	                alist[i] = alist[i+1]
	                alist[i+1] = temp

	def shuffle(x):
	    x = list(x)
	    random.shuffle(x)
	    return x
					
	def arrange(blist,item,num):
			found = False
			i=0
			
			while not found:
				if item==blist[i] or str(item)==str(blist[i]):
					blist.insert(num,blist.pop(i))
					found = True
				i+=1
			#print arrlist
			#print blist
			return blist
					
	def arrangementInd(clist,listEle,iteration):
		if iteration==0:
			type_of_arrangement=int(np.random.choice([1,2],1))
		else:
			type_of_arrangement=int(listEle)
		if type_of_arrangement==2:
			clist.reverse()            
		return type_of_arrangement

	def arrangementWhole(clist,type_of_arrangement1):
		#raw_input("Type - 1 : Straight\nType - 2 : Alternatively\nType - 3 : No particular order\n")
		#print "type of arrangement is ",type_of_arrangement1		
		if type_of_arrangement1==2:
				
				maxl = len(clist[0])
				for i in range(1,len(clist)):
				    if len(clist[i]) > maxl: maxl = len(clist[i])
		
				vals = []
				for i in range(0,maxl):
				    for j in range(0,len(clist)):
				        if len(clist[j]) > i:
				            vals.append(clist[j][i])
				return vals,int(type_of_arrangement1)
		else:
			clist=[inner for outer in clist for inner in outer]
			return clist,int(type_of_arrangement1)

	def printquestion(sortedList1,inputList1,inputList2,questionlist,optionlist,number_of_questions):
	 	sentences=['A Machine arranges the given input in the following way.','Input - ',' is the last step of the given input.','Answer the following questions for the below input:','Input - ','Answer key:']
	 	firstlist=[]
	 	for i in range(len(sortedList1)):
	 		firstlist.append(str('Step-')+str(i+1)+str(' : ')+str(sortedList1[i]))
	 	questionslist=[]
	 	for i in range(number_of_questions):
	 		questionslist.append(str(i+1)+str('. ')+str(questionlist[i]+'\n'+str('(a)'+optionlist[i][0]+'\n'+'(b)'+optionlist[i][1]+'\n'+'(c)'+optionlist[i][2]+'\n'+'(d)'+optionlist[i][3]+'\n'+'(e)'+optionlist[i][4])))
	 	text=str('\n'.join(final_output)+'\n\n'+sentences[0])+str('\n')+str(sentences[1])+str(' '.join(inputList1)+'\n')+str('\n'.join(firstlist)+'\n')+str('Step-')+str(len(sortedList1))+str(sentences[2]+'\n\n')+str(sentences[3]+'\n')+str(sentences[4])+str(' '.join(inputList2)+'\n\n')+str('\n\n'.join(questionslist)+'\n\n\n'+"_______________Next Set__________________"+'\n\n\n')
	 	return text
	 	

	def createinput():
		set_count = np.random.choice([1,2],1,p=[0.25,0.75])
		set_count=set_count[0]
		sets_list=[]
		elements_words=np.array([1,2,3,5,6])
		elements_numbers=np.array([9,10,11,12])
		words_list=np.random.choice(elements_words,2,replace=False,p=[0.3,0.1,0.3,0.2,0.1])
		words_list=list(words_list)
		numbers_list=np.random.choice(elements_numbers,2,replace=False,p=[0.3,0.2,0.1,0.4])	
		numbers_list=list(numbers_list)
		ind_set_count2=np.array([4,5,6])
		ind_set_count3=np.array([3,4])
		ind_set=[]
		if set_count==2:
			sets_list.append(words_list.pop())
			sets_list.append(numbers_list.pop())
			for i in list(np.random.choice(ind_set_count2,2)):
				ind_set.append(i)
		else:
			sets_list.append(words_list.pop())
			sets_list.append(numbers_list.pop())
			temp2=list(np.random.choice(ind_set_count3,1))
			for i in range(3):
				ind_set.append(temp2[0])
			temp=random.random()
			if int(math.ceil(2*temp))==1:
				sets_list.append(words_list.pop())
			else:
				sets_list.append(numbers_list.pop())

		return list(sets_list),ind_set

	def createlist(iteration,Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sets_list,ind_set):
		#Type - 1 : Words arranged alphabetically\nType - 2 : Words arranged alphabetically based on last letter\nType - 3 : Words arranged starting with vowels\nType - 4 : Words arranged starting with consonants\nType - 5 : Words arranged with number of vowels in them\nType - 6 : Words arranged with number of consonants in them\nType - 7 : Words arranged in no particular order\nType - 8 : Numbers arranged in no particular order\nType - 9 : Numbers arranged according to their value\nType - 10 : Prime numbers\nType - 11 : Composite numbers\nType - 12 : Numbers based on some function\n
		finalList=[]
		iterationValue=0
		subsetValue=1
		ind_set1=tuple(ind_set)
		sets_list1=tuple(sets_list)
		index_print=1

		while len(sets_list)!=0:
			er=0
			Type_of_subset1=str(sets_list.pop())
			input_value=[]
			if iteration==0:
				Type_of_subset.append(Type_of_subset1)
			else:
				Type_of_subset1=Type_of_subset[iterationValue]
				iterationValue+=1
			if Type_of_subset1=='1':	#for type 1
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				for line in fh:
					samplewords=line.split()
				alist = [ samplewords[i] for i in (random.sample(xrange(len(samplewords)), int(input_value[1])))]	
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				bubbleSort(alist)
			elif Type_of_subset1=='2':	#for type 2 
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				for line in fh:
					samplewords=line.split()
				alist = [ samplewords[i] for i in (random.sample(xrange(len(samplewords)), int(input_value[1])))]
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				blist=tuple(alist)
				for item in range(len(alist)):
					alist[item]=alist[item][::-1]
				bubbleSort(alist)
				for item in range(len(alist)):
					alist[item]=alist[item][::-1]

			elif Type_of_subset1=='3':#for type 3
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				samplewordsvowel=[]
				for line in fh:
					samplewords=line.split()
				for i in range(len(samplewords)):
					t=samplewords[i]
					
					if t[0] in ['a','e','i','o','u']:
						samplewordsvowel.append(samplewords[i])
				alist = [ samplewordsvowel[i] for i in (random.sample(xrange(len(samplewordsvowel)), int(input_value[1])))]
				if iteration==0:
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				bubbleSort(alist)
			elif Type_of_subset1=='4':#for type 4
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				samplewordsconsonants=[]
				for line in fh:
					samplewords=line.split()
				for i in range(len(samplewords)):
					t=samplewords[i]
					if t[0] not in ['a','e','i','o','u']:
						samplewordsconsonants.append(samplewords[i])
				alist = [ samplewordsconsonants[i] for i in (random.sample(xrange(len(samplewordsconsonants)), int(input_value[1])))]
				if iteration==0:
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				bubbleSort(alist)
			elif Type_of_subset1=='5':#for type 5
				if iteration==0:	
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				samplewordsvowel=[]
				for line in fh:
					samplewords=line.split()
				for i in range(len(samplewords)):
					t=samplewords[i]
					j=0
					foundvowel = False
					while j<len(t) and not foundvowel:
						if t[j] in ['a','e','i','o','u']:
							#print "Hola"
							foundvowel=True
							samplewordsvowel.append(samplewords[i])
						j+=1
				alist = [ samplewordsvowel[i] for i in (random.sample(xrange(len(samplewordsvowel)), int(input_value[1])))]
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				alist_rank=[]
				blist=[]
				for item in alist:
					count=0
					for letter in item:
						if letter in ['a','e','i','o','u']:
							count+=1
					alist_rank.append(count)
				for i in range(len(alist)):
					blist.append(alist[alist_rank.index(min(alist_rank))])
					alist_rank[alist_rank.index(min(alist_rank))]=float('inf')
				alist=blist	
			elif Type_of_subset1=='6':#for type 6
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				samplewordsconsonant=[]
				for line in fh:
					samplewords=line.split()
				for i in range(len(samplewords)):
					t=samplewords[i]
					j=0
					foundconsonant = False
					while j<len(t) and not foundconsonant:
						if t[j] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
							#print "Hola"
							foundconsonant=True
							samplewordsconsonant.append(samplewords[i])
						j+=1
				alist = [ samplewordsconsonant[i] for i in (random.sample(xrange(len(samplewordsconsonant)), int(input_value[1])))]
				if iteration==0:
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				alist_rank=[]
				blist=[]
				for item in alist:
					count=0
					for letter in item:
						if letter in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
							count+=1
					alist_rank.append(count)
				for i in range(len(alist)):
					blist.append(alist[alist_rank.index(min(alist_rank))])
					alist_rank[alist_rank.index(min(alist_rank))]=float('inf')
				alist=blist
			elif Type_of_subset1=='7':#for type 7
				if iteration==0:	
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				fh=open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\samplewords.txt", "r")
				for line in fh:
					samplewords=line.split()
				alist = [ samplewords[i] for i in (random.sample(xrange(len(samplewords)), int(input_value[1])))]
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
			elif Type_of_subset1=='8':#for type 8
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				samplenumbers=[i for i in range(1,1000)]
				alist = [ samplenumbers[i] for i in (random.sample(xrange(len(samplenumbers)), int(input_value[1])))]
				if iteration==0:
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
			elif Type_of_subset1=='9':#for type 9
				if iteration==0:
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				samplenumbers=[i for i in range(1,1000)]
				alist = [ samplenumbers[i] for i in (random.sample(xrange(len(samplenumbers)), int(input_value[1])))]
				if iteration==0:
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				quickSort(alist)
			elif Type_of_subset1=='10':#for type 10
				if iteration==0:	
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				prime_numbers=[]
				for num in range(2,301):#code to generate prime no's
				    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
				       prime_numbers.append(num)
				
				alist = [ prime_numbers[i] for i in (random.sample(xrange(len(prime_numbers)), int(input_value[1])))] 
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				quickSort(alist)
			elif Type_of_subset1=='11':#for type 11
				if iteration==0:	
					input_value.append('0')
					input_value.append(str(ind_set.pop()))
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
				prime_numbers=[]
				for num in range(2,301):#code to generate prime no's
				    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
				       prime_numbers.append(num)
				numbers_list=[i for i in range(2,301)]
				composite_numbers=list(set(numbers_list)-set(prime_numbers))
				alist = [ composite_numbers[i] for i in (random.sample(xrange(len(composite_numbers)), int(input_value[1])))]
				if iteration==0:	
					Subset_input.append(input_value[0])
					Subset_input.append(input_value[1])
				quickSort(alist)
			elif Type_of_subset1=='12':#for type 12
				nsp=NumericStringParser()
				if iteration==0:	
					nsp=NumericStringParser()
					expression_list=['2*x','(2*x)+1','x^2','x^3','2^x','(x^2)-1','(x^3)+1']
					expression=str(expression_list[np.random.choice(len(expression_list),1)])
					#print expression
					count=(ind_set.pop())
				else:
					input_value.append('0')
					input_value.append(str(Subset_input[subsetValue]))
					subsetValue+=2
					
				if iteration==0:	
					Subset_input.append(str(expression))
					Subset_input.append(str(count))
				else:
					expression=str(Subset_input[subsetValue-3])
					count=int(input_value[1])
					#print expression
				#countlist=random.sample(range(1, 10), count)
				#print countlist
				intialvalue=random.sample(range(1, 5), 1)
				#print intialvalue
				countlist=[]
				for i in range(count):
					countlist.append(intialvalue[0])
					intialvalue[0]+=1
				#print countlist
				alist=[]
				for i in (countlist):
					bexpression=[]
					expression=list(expression)
					for j in range(len(expression)):
						if expression[j]=='x' or expression[j]=='X':
							bexpression.append(str(i+1))
						else:
							bexpression.append(expression[j])
					bexpression=str(''.join(bexpression))
					alist.append(int(nsp.eval(bexpression)))
					quickSort(alist)
			else:
				print "Invalid input"
			

			if iteration==0:	
				Type_of_arrangement.append(arrangementInd(alist,Type_of_arrangement,iteration))
				dict_type_of_subset={'1' : 'Words arranged alphabetically','2' : 'Words arranged alphabetically based on last letter','3' : 'Words arranged starting with vowels', '4' : 'Words arranged starting with consonants', '5' : 'Words arranged with number of vowels in them', '6' : 'Words arranged with number of consonants in them','7': 'Words arranged in no particular order','8' : 'Numbers arranged in no particular order', '9' : 'Numbers arranged according to their value', '10' : 'Prime numbers','11' : 'Composite numbers', '12' : 'Numbers based on some function'}
				dict_type_of_arrangement_indset={1:'Increasing',2:'Decreasing'}
				kle="Subset - {} :''{}'' in {} order".format(index_print,dict_type_of_subset[Type_of_subset1],dict_type_of_arrangement_indset[Type_of_arrangement[index_print-1]])
				final_output.append(kle)
				index_print+=1
				if Type_of_subset1=='12':
					kle2=str("Function is {}".format(''.join(expression)))
					final_output.append(kle2)
			else:
				arrangementInd(alist,Type_of_arrangement[er],iteration)
				er+=1
			finalList.append(alist)
			outputList=tuple(finalList)
	
		if iteration==0:	
			if Number_of_sets==2:
				type_of_arrangement = int(np.random.choice([1,2],1,p=[0.8,0.2]))

			else:
				type_of_arrangement=2
			Type_of_arrangement_input.append(type_of_arrangement)
			dict_Number_of_sets={1:'One',2:'Two',3:'Three'}
			dict_type_of_arrangement={1:'Straight',2:'Alternatively'}
			
			final_output.append(str("Problem has {} subsets arranged {}.".format(dict_Number_of_sets[Number_of_sets],dict_type_of_arrangement[type_of_arrangement])))
			#print final_output
		else:
			type_of_arrangement=Type_of_arrangement_input[0]
			Type_of_arrangement_input.pop(0)		
		finalList,type_of_arrangement1=arrangementWhole(finalList,type_of_arrangement)
		for i in range(len(finalList)):
			finalList[i]=str(finalList[i])
		

			
		#inputList=raw_input("Enter 0th step\n").split()
		inputlist1='0'
		if inputlist1=='0':
			inputList=shuffle(finalList)
		else:
			inputList=inputlist1.split()

		outputList=list(outputList)
		#print "Final list is ",finalList
		#print "Input List is ",inputList
		#print "output List is",outputList
		tupleinputlist=tuple(inputList)
		inputList=list(inputList)
		sortedListnew=[]

		def execute1():#for alternate formation
			i=0
			j=0
			k=0
			sorted1=False
			while not sorted1:
				
				while (i<len(outputList))and not sorted1:
					
					if j<len(outputList[i]):
						
						#print inputList
						if (inputList==finalList):
							sorted1=True
						else:
							arrange(inputList,outputList[i][j],k)	#print "Hola"
							sortedListnew.append(" ".join(inputList))

						i+=1
						k+=1
					else:
						i+=1
						
				i=0	
				j+=1

				
		def execute2():#for number of sets equals to 2
				
			k=[]
			k.append([item for item in range(int((len(outputList[0]))))])
			k.append([(len(finalList)-1-item) for item in range(int(len(outputList[1])))])
			i=0
			j=0
			sorted1=False
			while not sorted1:
				while(i<len(outputList)and not sorted1):
					if j<len(outputList[i]):
						arrange(inputList,outputList[i][k[i][j]-len(outputList[0])],k[i][j])
						i+=1
						if (inputList==finalList):
							sorted1=True
						sortedListnew.append(" ".join(inputList))
						#print " ".join(inputList)
					else:
						i+=1
				i=0
				j+=1
		#print "Number_of_sets are {}".format(Number_of_sets)
		if Number_of_sets!=2:
			execute1()
			#print "Hola"
		else:
			#print type(type_of_arrangement1)
			if type_of_arrangement1==2:

				execute1()
				#print "Hola inside alternating sets"
			else:	
				execute2()
				#print "Hola inside same sets"


		sortedList=[]
		for i in sortedListnew:
		       if i not in sortedList:
		          sortedList.append(i)
		if sortedList[0]==inputList:
			sortedList.pop(0)
		#for i in sortedList:
		#	print i
		return Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sortedList,list(tupleinputlist),list(sets_list1),list(ind_set1)
	iteration=0
	sets_list,ind_set=createinput()
	#print "sets_list is {}".format(sets_list)
	Number_of_sets=len(sets_list)
	Type_of_subset=[]
	Type_of_arrangement=[]
	Type_of_arrangement_input=[]
	Subset_input=[]
	Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sortedList1,inputList1,sets_list,ind_set=createlist(iteration,Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sets_list,ind_set)
	global sortedList1_length
	sortedList1_length=len(sortedList1)
	#print Subset_input
	#print Subset_input[1]
	iteration=1
	Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sortedList,inputList2,sets_list,ind_set=createlist(iteration,Number_of_sets,Type_of_subset,Subset_input,Type_of_arrangement,Type_of_arrangement_input,sets_list,ind_set)
	global sortedList_length
	sortedList_length=len(sortedList)
	#print "inputList1 is : ",inputList1
	#print "sortedList1 is : ",sortedList1
	#print "inputList2 is : ",inputList2
	numberlist=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
	done=1
	questionlist=[]
	optionlist=[]
	num=0
	number_of_questions=0
	question_type_list=list(np.random.choice(['1','2','3','4','5','6'],5,replace=False))
	#print question_type_list
	while num<5:
		number_of_questions+=1
		#raw_input("Press enter to continue....")
		#print ("Enter type of the question from following list ")
		question_type=question_type_list[num]
		#"Type 1 : How many steps are required to sort it?\nType 2 : What is step X?\nType 3 : In which step do we get following order?\nType 4 : In step X, what is Yth element from left/right\nType 5 : what is position of element X in step Y\nType 6 : In step X what are the number of words between A and B?\nType 0 if you want to exit \n"
		if question_type=='1':
			#print "Number of steps required to sort is : ",len(sortedList)
			options = [ numberlist[i] for i in (random.sample(xrange(max(5,len(sortedList)+1)), 5))]
			if numberlist[len(sortedList)] not in options:
				options[random.randrange(0,len(options))]=numberlist[len(sortedList)]
				#print "Hola"
			#print options
			optionlist.append(options)
			questionlist.append('How many steps are required to sort it?')
		elif question_type=='2':
			step=np.random.choice(len(sortedList),1)
			#print "Step {} is : \n".format(step),sortedList[step-1]
			options = [ sortedList[i] for i in (random.sample(xrange(len(sortedList)), min(5,len(sortedList))))]
			if sortedList[step-1] not in options:
				options[random.randrange(0,len(options))]=sortedList[step-1]
				#print "Hola"
			#print options
			question2='What is step {}?'.format(step)
			questionlist.append(question2)
			optionlist.append(options)
		elif question_type=='3':
			#print sortedList
			order1=sortedList[np.random.choice(len(sortedList),1)]
			#print "In step - {} we get above order : ".format(sortedList.index(order1)+1)

		
			options = [ numberlist[i] for i in (random.sample(xrange(max(5,len(sortedList)+1)), 5))]
			if numberlist[sortedList.index(order1)+1] not in options:
				options[random.randrange(0,len(options))]=numberlist[sortedList.index(order1)+1]
				#print "Hola"
			#print options
			question3='In which step do we get following order? \n {}'.format(order1)
			questionlist.append(question3)
			optionlist.append(options)
		elif question_type=='4':
			X=np.random.choice(len(sortedList),1)
			list12=[i for i in range(1,(len(sortedList)+1))]
			Y=int(np.random.choice(list12,1))
			gh=str(np.random.choice(['left','right'],1)[0])
			listelement=sortedList[X-1].split()
			#print listelement

			options = [ listelement[i] for i in (random.sample(xrange(len(listelement)), min(5,len(listelement))))]
			if gh=='left':	
				if listelement[Y-1] not in options:
					options[random.randrange(0,len(options))]=listelement[Y-1]
					#print "Hola"
			else:
				if listelement[len(listelement)-Y] not in options:
					options[random.randrange(0,len(options))]=listelement[len(listelement)-Y]
					#print "Hola"
			#print options
			question4='In step {}, what is no-({}) element from {}?'.format(X,Y,gh)
			questionlist.append(question4)
			optionlist.append(options)
		elif question_type=='5':
			X=np.random.choice(len(sortedList),1)
			listelement=sortedList[X-1].split()
			gh=listelement[np.random.choice(len(listelement),1)]
			for i in range(len(listelement)):
				if listelement[i]==gh:
					ph=i+1
					break
			#print "Element is at position - {} in step - {}".format(ph,X)
			options = [ numberlist[i] for i in (random.sample(xrange(max(5,len(listelement))), 5))]
			if numberlist[ph] not in options:
				options[random.randrange(0,len(options))]=numberlist[ph]
				#print "Hola"
			#print options
			question5='What is the position of the element ''{}'' in step - {}?'.format(gh,X)
			questionlist.append(question5)
			optionlist.append(options)
		elif question_type=='6':
			X=np.random.choice(len(sortedList))
			Z=np.random.choice(len(sortedList),2,replace=False)
			listelement=sortedList[X-1].split()
			gh=listelement[Z[0]]
			fh=listelement[Z[1]]
			if listelement.index(gh)<listelement.index(fh):
				temp321=gh
				gh=fh
				fh=temp321
			value=abs(listelement.index(gh)-listelement.index(fh))
			#print "There are {} words between {} and {} in step - {}".format(value,gh,fh,X)
			options = [ numberlist[i] for i in (random.sample(xrange(max(5,len(listelement))), 5))]
			if numberlist[value] not in options:
				wer=random.randrange(0,len(options))
				options[wer]=numberlist[value]
				#print "Hola"
				#print wer
			#print options
			question6='In step {} what are the number of words between ''{}'' and ''{}''?'.format(X,gh,fh)
			questionlist.append(question6)
			optionlist.append(options)
		else:
			print "error in input"
		num+=1
	text=printquestion(sortedList1,inputList1,inputList2,questionlist,optionlist,number_of_questions)
	return text

steps_Length=input('Enter minimum number of steps : ')
countFinal=input('Enter number of sets to be written : ')
sets_count=0
while sets_count<countFinal:
	
	try:
		text=str('\nSet {}\n\n').format(sets_count+1)+mainFunction()
		#print "Set {}".format(i+1)
		if (steps_Length<sortedList1_length and sortedList1_length<steps_Length+2) and (steps_Length<sortedList_length and sortedList_length<steps_Length+2):	
			file = open("C:\Users\Olive\Desktop\oliveboard\project_Ipop\sampleQuestions.txt", "a")
		 	file.write(text)
		 	file.close()
		 	sets_count+=1
	except:
		print ('\n')+"Error in Set {}".format(sets_count+1)
		print '\n'.join(final_output)+('\n')
		pass