import numpy as np
import random,os,math
from fractions import *
from itertools import combinations,permutations


def createEquation():
	def createCoefficients():
		global a,b,c,d
		integers=[x for x in range(-9,10)]
		integers_without_zero=[x for x in integers if x!=0]
		a=int(np.random.choice(integers_without_zero,1))
		c=int(np.random.choice(integers_without_zero,1))
		temp=random.randint(1,4)
		if temp==1:
			b=1
			d=int(np.random.choice(integers_without_zero,1))
		elif temp==2:
			d=1
			b=int(np.random.choice(integers_without_zero,1))
		elif temp==3:
			d=int(np.random.choice(integers_without_zero,1))
			b=int(np.random.choice(integers_without_zero,1))
		else:
			b=1
			d=1
		return [b*d,-1*((a*d)+(b*c)),a*c]
	coefficients=createCoefficients()
	while coefficients[1]==0:
		coefficients=createCoefficients()
	while math.fabs(coefficients[0])>10 or math.fabs(coefficients[2])>40:
		coefficients=createCoefficients()
	divide=reduce(gcd,coefficients)
	while divide not in [1,-1]:
		coefficients=createCoefficients()
		divide=reduce(gcd,coefficients)
	coefficients=[x/divide for x in coefficients]
	if coefficients[0]<0:
		coefficients=[-1*x for x in coefficients]
	r1=Fraction(a,b)
	r2=Fraction(c,d)
	roots=[r1,r2]
	return roots,coefficients,[a,b,c,d]

def correctCoeff(coeff):
	if coeff==1:
		coeff='+'
	elif coeff==-1:
		coeff='-'
	elif coeff>0:
	#	coeff='-'+str(coeff)
	#else:
		coeff='+'+str(coeff)
	return coeff

def createSolution(coeffList,constant):
	a=coeffList[0]
	b=coeffList[1]
	c=coeffList[2]
	d=coeffList[3]
	#c1,c2,c3,c4,c5,c6='','','','','',''
	c1=b*d
	c2=-1*((a*d)+(b*c))
	c3=a*c
	if c1<0:
		c1*=-1
		c2*=-1
		c3*=-1
	if c1==1:
		c1=''
	c2=correctCoeff(c2)
	if c3>0:
		c3='+'+str(c3)
	firstLine='%s%s%s%s%s%s=0'%(c1,constant,u"\u00B2",c2,constant,c3)

	c1=b*d
	c3=-1*(a*d)
	c2=-1*(b*c)
	c4=a*c
	if c1<0:
		c1*=-1
		c2*=-1
		c3*=-1
		c4*=-1
	if c1==1:
		c1=''
	c2=correctCoeff(c2)
	c3=correctCoeff(c3)
	if c4>0:
		c4='+'+str(c4)
	secondLine='%s%s%s%s%s%s%s%s=0'%(c1,constant,u"\u00B2",c2,constant,c3,constant,c4)

	c1=b
	c2=d
	c3=-1*c
	c4=-1*a
	if c1==1:
		c1=''
	elif c1==-1:
		c1='-'
	if c2==1:
		c2=''
	elif c2==-1:
		c2='-'
	if c3>0:
		c3='+'+str(c3)
	if c4>0:
		c4='+'+str(c4)
	thirdLine='%s%s(%s%s%s)%s(%s%s%s)=0'%(c1,constant,c2,constant,c3,c4,c2,constant,c3)	
	fourthLine='(%s%s%s)(%s%s%s)=0'%(c1,constant,c4,c2,constant,c3)

	root1=Fraction(a,b)
	root2=Fraction(c,d)
	fifthLine='%s = %s or %s'%(constant,root1,root2)
	text='%s\n->%s\n->%s\n->%s\nThus we get, %s'%(firstLine,secondLine,thirdLine,fourthLine,fifthLine)
	if root1==root2:
		text=text[:len(text)-5]
	return text




def checkAnswer(eq1_r1,eq1_r2,eq2_r1,eq2_r2):
	if (eq1_r1>eq2_r1 and eq1_r1>eq2_r2) and (eq1_r2>eq2_r1 and eq1_r2>eq2_r2):
		return 'gt'
	elif (eq1_r1<eq2_r1 and eq1_r1<eq2_r2) and (eq1_r2<eq2_r1 and eq1_r2<eq2_r2):
		return 'lt'
	elif (eq1_r1>=eq2_r1 and eq1_r1>=eq2_r2) and (eq1_r2>=eq2_r1 and eq1_r2>=eq2_r2):
		return 'gte'
	elif (eq1_r1<=eq2_r1 and eq1_r1<=eq2_r2) and (eq1_r2<=eq2_r1 and eq1_r2<=eq2_r2):
		return 'lte'
	else:
		return 'nr'

def createQuestion():
	eq1=createEquation()
	solution1=createSolution(eq1[2],'x')
	eq2=createEquation()
	solution2=createSolution(eq2[2],'y')
	eq1_r1=eq1[0][0]
	eq1_r2=eq1[0][1]
	eq2_r1=eq2[0][0]
	eq2_r2=eq2[0][1]
	answer=checkAnswer(eq1_r1,eq1_r2,eq2_r1,eq2_r2)
	return [eq1,eq2,answer,solution1,solution2]

def createSet():
	resultChoiceList=['lt','lte','gt','gte','nr']
	resultList=list(np.random.choice(resultChoiceList,1))
	question=createQuestion()
	answer=question[2]
	while answer!=resultList[0]:
		question=createQuestion()
		answer=question[2]
	return question

def createText(question):
	if question[0][1][0]==1:
		eq1_c1=''
	else:
		eq1_c1=str(question[0][1][0])
	if question[0][1][1]==1:
		eq1_c2='+'
	elif question[0][1][1]==-1:
		eq1_c2='-'
	elif question[0][1][1]<0:
		eq1_c2=str(question[0][1][1])
	else:
		eq1_c2='+'+str(question[0][1][1])
	if question[0][1][2]<0:
		eq1_c3=str(question[0][1][2])
	else:
		eq1_c3='+'+str(question[0][1][2])
	if question[1][1][0]==1:
		eq2_c1=''
	else:
		eq2_c1=str(question[1][1][0])
	if question[1][1][1]==1:
		eq2_c2='+'
	elif question[1][1][1]==-1:
		eq2_c2='-'
	elif question[1][1][1]<0:
		eq2_c2=str(question[1][1][1])
	else:
		eq2_c2='+'+str(question[1][1][1])
	if question[1][1][2]<0:
		eq2_c3=str(question[1][1][2])
	else:
		eq2_c3='+'+str(question[1][1][2])
	equation1='%sx%s%sx%s = 0 '%(eq1_c1,u"\u00B2",eq1_c2,eq1_c3)
	equation2='%sy%s%sy%s = 0 '%(eq2_c1,u"\u00B2",eq2_c2,eq2_c3)
	key=['lte','gte','lt','gt','nr'].index(question[2])+1
	text=''
	text+='%s\n%s\n(1) If x %s y\n(2) If x %s y\n(3) If x < y\n(4) If x > y\n(5) If x = y or no specific relation can be established.\nAnswer key: %s\n\nSolution:\nFirst equation - \n%s\n\nSecond equation - \n%s\n\nHence option %s\n\n'%(equation1,equation2,u"\u2264",u"\u2265",key,question[3],question[4],key)
	return text

commontext='Based on the set of equations given, Choose the conclusion.\n\n'
fn = os.path.join(os.path.dirname(__file__), 'sampleQuestions.txt')
file = open(fn, "a")
file.write(commontext.encode('utf8'))
countFinal=input('Enter number of questions to be written : ')
sets_count=0
while sets_count<countFinal:
	question=createSet()
	question_text=createText(question)
	text='%s: '%(sets_count+1)
	text+=(question_text)
	#print "Set {}".format(i+1)
 	file.write(text.encode('utf8'))
 	sets_count+=1
file.close()
print 'Done. Output written to file : {} '.format(fn)