done=1
while done!='0':
	raw_input("Press enter to continue....")
	print ("Enter type of the question from following list ")
	question_type=raw_input("Type 1 : How many steps are required to sort it?\nType 2 : What is step X?\nType 3 : In which step do we get following order?\nType 4 : In step X, what is Yth element from left/right\nType 5 : what is position of element X in step Y\nType 6 : In step X what are the number of words between A and B?\nType 0 if you want to exit \n")
	done=question_type
	if question_type=='1':
		print "Number of steps required to sort is : ",len(sortedList)
	elif question_type=='2':
		step=int(raw_input("Enter the step no. : "))
		print "Step {} is : \n".format(step),sortedList[step-1]
	elif question_type=='3':
		order1=raw_input("Enter the order without any quotes ")
		print "In step - {} we get above order : ".format(sortedList.index(order1)+1)
	elif question_type=='4':
		X=int(raw_input("Enter step no."))
		Y=int(raw_input("Enter the position no. of the element wrt left/right "))
		gh=raw_input("Postion is from left or right?(Enter all in small caps) ")
		listelement=sortedList[X-1].split()
		#print listelement
		if gh=='left':
			print "Element in step - {} at postion - {} from {} is : {}".format(X,Y,gh,listelement[Y-1])
		else:
			print "Element in step - {} at postion - {} from {} is : {}".format(X,Y,gh,listelement[len(listelement)-Y])
	elif question_type=='5':
		X=int(raw_input("Enter step no."))
		gh=raw_input("What is the element?(Enter all in small caps")
		listelement=sortedList[X-1].split()
		for i in range(len(listelement)):
			if listelement[i]==gh:
				ph=i+1
				break
		print "Element is at position - {} in step - {}".format(ph,X)
	elif question_type=='6':
		X=int(raw_input("Enter step no."))
		gh=raw_input("What is the first element?(Enter all in small caps)")
		fh=raw_input("What is the second element?(Enter all in small caps)")
		listelement=sortedList[X-1].split()
		value=abs(listelement.index(gh)-listelement.index(fh))
		print "There are {} words between {} and {} in step - {}".format(value,gh,fh,X)
	else:
		if question_type!='0':
			print "error in input"
		