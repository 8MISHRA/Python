'''def sum(lst):
	"""Returns : the sum of all elements in lst 
	precondition: lst is a list of all numbers
	(either floats or ints)
	"""
	#create a variable to hold the result(start at 0)
	#for each element in the list 
	#chek if it is an int
	#add 1 if it is
	#return the variable 
	result = 0

	for x in lst:
		if type(x) == int: 
			result = result + 1

	return result		

print(sum([2.4,154.23,4,7,'hello',2]))'''

'''def despace(s):
	"""Returns: s but with its spaces removed 
	Precondition:s is a string
	"""
	#Create an empty string accumulator
	#For each charector x of s
	  #chek if x is a space 
	  #add it to accumulator if it is not

	result = ''
	for x in s:
		if x !=' ':
			result = result + x

	return result'''

'''
def reverse(s):
	"""Returns:copy of s with charecters reversed.

	Example: reverse('Hello') returns 'olleH' 
	Precondition: s is a (Possibly empty string)"""
	result = ''
	for x in s:
		result =  x + result 
	return result

print(reverse("w o r k"))
print(reverse('Hello'))'''

'''def copy_add_one(lst):
	"""Returns: copy with 1 added to every element
	precondition: lst is a list of all numbers 
	(either floats or ints)"""
	#create an empty list accumulator
	copy = []
	for x in lst:
		print(id(copy))
		x = x+1
		copy.append(x)
		print(id(copy))
	
	return copy
lst = [1,2,3,4]
print(copy_add_one(lst))
print(lst)
'''

'''def hello(n):
	"""Prints 'Hello World' n times
	Precondition: n>0 is an int
	"""
	for x in range(n):
		print('Hello World')
	
'''
# def sum_squares(n):
# 	"""
# 	Returns: sum of sqrs to n
# 	Precondition: n is int >0
# 	"""
# 	y = 0
# 	for x in range(n+1):
# 		y = y + x*x
		
# 	return y

# print(sum_squares(1000

# def partition(s):
# 	"""Returns : a list splitting s in two parts 

# 	The first element of the list in chars in even positions (starting at 0), while the second is odds.

# 	Examples: 
# 	  partition('abcde') is ['ace', 'bd']
# 	  partition('aabb') is ['ab', 'ab']

# 	Precondition: s is a string
# 	"""
# 	#create an acc. for first and second
# 	#separate the even places chars and same with odds as a list
# 	#add the both list
# 	#return the list with two parts
# 	frst = ''
# 	scnd = ''
# 	n = len(s)
# 	for x in range(n):
# 		if x%2 == 0:
# 			frst = frst + s[x]
# 		else:
# 			scnd = scnd + s[x]

# 	return [frst, scnd]
	
# print(partition('hello'))
# print(partition('Divyansh'))


# def add_one(lst):
# 	"""(Procedure)Adds 1 to every element in the list
# 	precondition: lst is a list of all numbers 
# 	(either floats or ints)"""
# 	#create an empty list accumulator
# 	for k in range(len(lst)):
# 		lst[k] = lst[k] + 1
	
# 	# Procedure no return

# def fibonacci(n):
# 	"""
# 	Returns: a febonacci series

# 	all the elements of the febonacci series are 
# 	the sum of the previous two elements of that seires

# 	Parameter: It is the number of terms in the 
# 	Precondition: n is a int and >0

# 	Example: 
# 	>>> fibonacci(1)
# 	0
# 	>>> fibonacci(2)
# 	[0,1]
# 	>>> fibonacci(3)
# 	[0,1,1]
# 	>>> fibonacci(4)
# 	[0,1,1,2]
# 	>>> fibonacci(5)
# 	[0,1,1,]
	


# 	"""
