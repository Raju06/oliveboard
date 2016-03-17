from sets import Set
from itertools import combinations

def createLeftList(left,left_input):
	left_list=[]
	for i in range(len(left)):
		list_i=[]
		for j in range(len(left_input)):
			if left[i] in left_input[j]:
				list_i.append(j+1)
			else:
				pass
		left_list.append(list_i)
	return left_list

def createRightList(right,right_input):
	right_list=[]
	for i in range(len(right)):
		list_i=[]
		for j in range(len(right_input)):
			if right[i] in right_input[j]:
				list_i.append(j+1)
			else:
				pass
		right_list.append(list_i)
	return right_list


temp=1
left_input=[]
right_input=[]
while temp!='0':
	left_input.append(raw_input("Enter left list\n").split())
	right_input.append(raw_input("Enter right list\n").split())
	temp=raw_input("Enter 0 if list is done : ")

left=[]
right=[]
for line in left_input:
	for item in line:
		if item not in left:
			left.append(item)
for line in right_input:
	for item in line:
		if item not in right:
			right.append(item)			


print left
print left_input
print right
print right_input
left_list=createLeftList(left,left_input)
right_list=createRightList(right,right_input)

print left_list
print right_list

'''print "solved left list is \n",solved_left_list
print "solved right list is \n",solved_right_list
print "unsolved left list is \n",unsolved_left_list
print "unsolved right list is \n",unsolved_right_list

for i in range(len(solved_left_list)):
	print "{} is {}".format(solved_left_list[i],solved_right_list[i]) 
#print "left list is {}".format(left_list)
#print "right list is {}".format(right_list)'''