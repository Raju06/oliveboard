from itertools import combinations
def compare(i,j,left,right):
	left_list=[]
	right_list=[]
	for i_item in left[i]:
		for j_item in left[j]:
			if i_item == j_item:
				left_list.append(i_item)

	for i_item in right[i]:
		for j_item in right[j]:
			if i_item == j_item:
				right_list.append(i_item)
	return left_list,right_list

def comparewhole(combinations_list,left,right):
	left_list=[]
	right_list=[]
	for i in range(len(combinations_list)):
		left_temp,right_temp=compare(combinations_list[i][0],combinations_list[i][1],left,right)
		left_list.append(left_temp)
		right_list.append(right_temp)
	return left_list,right_list

def separatesingle(left_list,right_list,left,right):
	final_left_list=[]
	final_right_list=[]
	i=0
	while i<(len(left_list)):
		if len(left_list[i])==1:
			if left_list[i][0] not in final_left_list:
				final_left_list.append(left_list[i].pop())
				final_right_list.append(right_list[i].pop())
			else:
				i+=1
		else: 
			if len(left_list[i])>1:
				if left_list[i] not in left:	
					left.append(left_list.pop(left_list.index(left_list[i])))
					right.append(right_list.pop(right_list.index(right_list[i])))
				else:
					left_list.pop(left_list.index(left_list[i]))
					right_list.pop(right_list.index(right_list[i]))

	return final_left_list,final_right_list



temp=1
left=[]
right=[]
while temp!='0':
	left.append(raw_input("Enter left list\n").split())
	right.append(raw_input("Enter right list\n").split())
	temp=raw_input("Enter 0 if list is done : ")

combinations_list=map(list,combinations([i for i in range(len(left))],2))
left_list,right_list=comparewhole(combinations_list,left,right)
final_left_list,final_right_list=separatesingle(left_list,right_list,left,right)


print "Main lists are : \n"
for i in range(len(left)):
	print "{} is {}".format(left[i],right[i]) 

for i in range(len(final_left_list)):
	print "{} is {}".format(final_left_list[i],final_right_list[i]) 
#print "left list is {}".format(left_list)
#print "right list is {}".format(right_list)
