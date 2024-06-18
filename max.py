count_frame = 0

def max_lst(lst):
	'''Returns maximum element from the given list

	'''
	assert len(lst) > 0, repr(lst) + ' is an empty list'
	# lst = [1,4,8,2,5]
	global count_frame 
	# base case 1
	if len(lst) == 1:
		count_frame += 1
		return lst[0]
		
	#base case 2
	elif len(lst) == 2:
		count_frame += 1
		return lst[0] if lst[0] > lst [1] else lst[1]
			
	elif len(lst) > 2:

		count_frame += 1

		#recurssive call
		left = max_lst(lst[:1])

		#recurssive call
		right = max_lst(lst[1:])
		return max(left, right)

print(max_lst([5,67,67,9]))

