from sets import Set
from itertools import combinations

def compare(i,j,left,right):
	
	left_set_i=set(left[i])
	left_set_j=set(left[j])
	right_set_i=set(right[i])
	right_set_j=set(right[j])

	left_list_intersection=list(left_set_i & left_set_j)
	right_list_intersection=list(right_set_i & right_set_j)
	
	left_list_subtract = list(left_set_i - left_set_j)
	right_list_subtract = list(right_set_i - right_set_j)
	return left_list_intersection,right_list_intersection,left_list_subtract,right_list_subtract


def comparewhole(combinations_list,left,right):
	solved_left_list=[]
	solved_right_list=[]
	unsolved_left_list=[]
	unsolved_right_list=[]
	for i in range(len(combinations_list)):
		left_intersection,right_intersection,left_subtract,right_subtract=compare(combinations_list[i][0],combinations_list[i][1],left,right)
		if len(left_intersection)==1 and left_intersection[0] not in solved_left_list:	
			solved_left_list.append(left_intersection[0])
			solved_right_list.append(right_intersection[0])
		if len(left_subtract)>1 and left_subtract not in unsolved_left_list:
			unsolved_left_list.append(left_subtract)
			unsolved_right_list.append(right_subtract) 
	return solved_left_list,solved_right_list,unsolved_left_list,unsolved_right_list

def removeSingleItems(left_list_single,right_list_single,left_main,right_main):
	left_list_unsolved=[]
	right_list_unsolved=[]
	for i in range(len(left_main)):
		temp_i=list(set(left_main[i])-set(left_list_single))
		temp_j=list(set(right_main[i])-set(right_list_single))
		temp_i_unsolved=list(set(left_main[i])&set(left_list_single))
		temp_j_unsolved=list(set(right_main[i])&set(right_list_single))
		if len(temp_i)==1 and temp_i not in left_list_single:
			left_list_single.append(temp_i[0])
			right_list_single.append(temp_j[0])
		if len(temp_i_unsolved)>1 and temp_i_unsolved not in left_list_unsolved:
			left_list_unsolved.append(temp_i_unsolved)
			right_list_unsolved.append(temp_j_unsolved) 
	return left_list_single,right_list_single,left_list_unsolved,right_list_unsolved





temp=1
left=[]
right=[]
while temp!='0':
	left.append(raw_input("Enter left list\n").split())
	right.append(raw_input("Enter right list\n").split())
	temp=raw_input("Enter 0 if list is done : ")


combinations_list=map(list,combinations([i for i in range(len(left))],2))
solved_left_list,solved_right_list,unsolved_left_list,unsolved_right_list=comparewhole(combinations_list,left,right)


solved_left_list,solved_right_list,unsolved_left_list,unsolved_right_list=removeSingleItems(solved_left_list,solved_right_list,unsolved_left_list,unsolved_right_list)
print "solved left list is \n",solved_left_list
print "solved right list is \n",solved_right_list
print "unsolved left list is \n",unsolved_left_list
print "unsolved right list is \n",unsolved_right_list

for i in range(len(solved_left_list)):
	print "{} is {}".format(solved_left_list[i],solved_right_list[i]) 
#print "left list is {}".format(left_list)
#print "right list is {}".format(right_list)