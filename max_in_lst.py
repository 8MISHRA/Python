count_frame = 0
"""Finding the max in a list - Write a recursive function that receives
 a non-empty list of integers and returns the value of the maximum
  element in the list. Enforce the precondition that the list be non-empty.
   Count the number of recursive calls made by the function.
  """
# def max_lst(lst):

# 	if len(lst) == 1:
# 		return lst[0]

# 	elif len(lst) == 2:
# 		 return lst[0] if lst[0] > lst[1] else lst[1]

# 	left = max_lst(lst[:2])
# 	right = max_lst(lst[2:])

# 	if left < right:
# 		return right
# 	return left

# print(max_lst([5,1,88,25,11]))

'''Palindrome - Write a recursive function that receives
 a string and returns True if it is a palindrome, and False otherwise.
  Enforce the precondition on the parameter.
   Count the number of recursive calls made by the function.
  '''

# def is_palindrome(s):
# 	global count_frame
# 	if len(s) <= 1:
# 		return True


# 	left = True if s[0] == s[-1] else False
# 	right = is_palindrome(s[1:-1])

# 	count_frame += 1
# 	return right and left

# print(is_palindrome('mam'))
# print(count_frame)

"""Sorted or not - Write a recursive function that receives 
a list of integers and returns True if it is sorted
 (in non-decreasing order), and False otherwise.
  Count the number of recursive calls made by the function.

 """

# def is_sorted(lst):

# 	lst = [1,2,4,3,9,8,6]

# 	if lst[0] < lst[1]:
# 		return False
		

# def let_gcd(a, b):

# 	global count_frame

# 	assert type(a) == int, str(repr(a)) + ' is not a number'
# 	assert type(b) == int, str(repr(b)) + ' is not a number'
# 	assert a>=0 and b >= 0 , str(repr(a)) + str(repr(b)) + ' one of them is negetive number'

# 	if a == 0:
# 		return b 
# 	elif b == 0:
# 		return a

# 	if a%b == 0:
# 		return b

# 	left = let_gcd(b, a%b)
# 	count_frame += 1
# 	return left 

# print(let_gcd(20, 20))
# print(count_frame)

count_call=0
def sort_list(lst):

	global count_call
	
	if len(lst)<=1 :
		return True
	
	# elif lst[0]<=lst[1]:
	# 	count_call=count_call+1
	# 	return sort_list(lst[1:])
	
	return lst[0]<=lst[1] and sort_list(lst[1:])

print(sort_list([0,7,1,1]))
print(count_call)