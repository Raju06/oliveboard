#defined functions
from __future__ import division
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                       ZeroOrMore,Forward,nums,alphas,oneOf)
import operator
import random
import math
from sets import Set
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


def arrangementInd(clist):
	type_of_arrangement=raw_input("Type - 1 : Ascending order\nType - 2 : Descending order\nType - 3 : No particular order\n")
	if type_of_arrangement=='2':
		clist.reverse()            

def arrangementWhole(clist):
	type_of_arrangement=raw_input("Type - 1 : Straight\nType - 2 : Alternatively\nType - 3 : No particular order\n")
	if type_of_arrangement=='2':
		
		maxl = len(clist[0])
		for i in range(1,len(clist)):
		    if len(clist[i]) > maxl: maxl = len(clist[i])

		vals = []
		for i in range(0,maxl):
		    for j in range(0,len(clist)):
		        if len(clist[j]) > i:
		            vals.append(clist[j][i])
	return vals  

finalList=[]
Number_of_sets=input("Enter number of subsets in the question : ")
Type_of_subset=[]
for i in range(Number_of_sets):
	print ("Enter the type of subset you wish to use from the following list")
	Type_of_subset1=raw_input("Type - 1 : Words arranged alphabetically\nType - 2 : Words arranged alphabetically based on last letter\nType - 3 : Words arranged starting with vowels\nType - 4 : Words arranged starting with consonants\nType - 5 : Words arranged with number of vowels in them\nType - 6 : Words arranged with number of consonants in them\nType - 7 : Words arranged in no particular order\nType - 8 : Numbers arranged in no particular order\nType - 9 : Numbers arranged according to their value\nType - 10 : Prime numbers\nType - 11 : Composite numbers\nType - 12 : Numbers based on some function\n")
	Type_of_subset.append(Type_of_subset1)
	if Type_of_subset1=='1':	#for type 1
		alist=raw_input("Enter the list of words in any order separated by single space(all letters must in small caps)\n").split()
		bubbleSort(alist)
	elif Type_of_subset1=='2':	#for type 2 
		alist=raw_input("Enter the list of words in any order separated by single space(all letters must in small caps)\n").split()
		blist=tuple(alist)
		for item in range(len(alist)):
			alist[item]=alist[item][::-1]
		bubbleSort(alist)
		for item in range(len(alist)):
			alist[item]=alist[item][::-1]

	elif Type_of_subset1=='3':#for type 3
		alist=raw_input("Enter the list of words beginning with vowels in any order separated by single space(all letters must in small caps)\n").split()
		bubbleSort(alist)
	elif Type_of_subset1=='4':#for type 4
		alist=raw_input("Enter the list of words beginning with consonants in any order separated by single space(all letters must in small caps)\n").split()
		bubbleSort(alist)
	elif Type_of_subset1=='5':#for type 5
		alist=raw_input("Enter the list of words containing vowels in any order separated by single space(all letters must in small caps)\n").split()
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
		alist=raw_input("Enter the list of words containing consonants in any order separated by single space(all letters must in small caps)\n").split()
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
		alist=raw_input("Enter the list of words in any order separated by single space(all letters must in small caps)\n").split()
	elif Type_of_subset1=='8':#for type 8
		alist=map(int,raw_input("Enter the list of numbers in any order separated by single space\n").split())		
	elif Type_of_subset1=='9':#for type 9
		alist=map(int,raw_input("Enter the list of numbers in any order separated by single space\n").split())
		quickSort(alist)
	elif Type_of_subset1=='10':#for type 10
		input_value=raw_input("Enter the list of numbers in any order separated by single space\n(Enter 0 X if you want to generate X random prime numbers)\n").split()       
		if input_value[0]!='0':        
			alist=map(int,input_value)       
		else:
			prime_numbers=[]
			for num in range(2,1001):#code to generate prime no's
			    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
			       prime_numbers.append(num)
			
			alist = [ prime_numbers[i] for i in (random.sample(xrange(len(prime_numbers)), int(input_value[1])))] 
			quickSort(alist)
	elif Type_of_subset1=='11':#for type 11
		input_value=raw_input("Enter the list of numbers in any order separated by single space\n(Enter 0 X if you want to generate X random Composite numbers)\n").split()       
		if input_value[0]!='0':        
			alist=map(int,input_value)       
		else:
			prime_numbers=[]
			for num in range(2,1001):#code to generate prime no's
			    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
			       prime_numbers.append(num)
			numbers_list=[i for i in range(2,1001)]
			composite_numbers=list(set(numbers_list)-set(prime_numbers))
			alist = [ composite_numbers[i] for i in (random.sample(xrange(len(composite_numbers)), int(input_value[1])))]
			quickSort(alist)
	elif Type_of_subset1=='12':#for type 12
		nsp=NumericStringParser()
		expression=raw_input("Enter the expression without any spaces\n")
		count=input("Enter count of numbers : ")
		alist=[]
		for i in range(count):
			bexpression=[]
			expression=list(expression)
			for j in range(len(expression)):
				if expression[j]=='x' or expression[j]=='X':
					bexpression.append(str(i+1))
				else:
					bexpression.append(expression[j])
			bexpression=str(''.join(bexpression))
			alist.append(int(nsp.eval(bexpression)))

	else:
		print "Invalid input"
	arrangementInd(alist)
	finalList.append(alist)
finalList=arrangementWhole(finalList)

print finalList