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

temp=1
left=[]
right=[]
while temp!='0':
	left.append(raw_input("Enter left list\n").split())
	right.append(raw_input("Enter right list\n").split())
	temp=raw_input("Enter 0 if list is done : ")

combinations_list=map(list,combinations([i for i in range(len(left))],2))
left_list,right_list=comparewhole(combinations_list,left,right)


for i in range(len(left_list)):
	print "{} is {}".format(left_list[i],right_list[i]) 
#print "left list is {}".format(left_list)
#print "right list is {}".format(right_list)
