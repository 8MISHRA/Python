# copy = []
# def flat(lst):

# 	# for i in range(len(lst[0])):
# 	# 		for j in lst:
# 	# 			print (j[i])

# 	# for i in range(len(lst[0])):
# 	# 	for j in range(len(lst)):
# 	# 		print(lst[i][j], end = ',')
	
# 	global copy
# 	for i in lst:
# 		if type(i) == list:
# 			flat(i)

# 		else:
# 			copy.append(i)
# 	return copy
		
# 	# return copy
	
# print(flat(lst))

# def all_nums(table):
# 	"""
# 	Returns True if table contains only numbers (int / float), False otherwise

# 	Prcondition: table is a (non - ragged) 2d list
# 	"""
	
# 	# here in this code we can use result = True as an accumulator and at last return result
# 	# BTW at last Result = False but the given code is optimal solution

# 	for row in table:

# 		for item in row:

# 			if not type(item) in [int, float]:
# 				return False
		
# 	return True				


# # print(all_nums(lst))

# def transpose(table):
# 	"""
# 	Returns: copy of table with rows and column swaped

# 	Prcondition: table is a (non - ragged) 2d list
# 	"""
# #	 # for i in range(len(lst[0])):
# #	 # 	# 	for j in range(len(lst)):
# #	 # 	# 		print(lst[i][j], end = ',')

# # 	result = []

# # 	for row in range(len(table[0])):

# # 		for column in range(len(table)):

# # 			result.append(table [row][column])
# # 	return result
# 	num_rows = len(table)   #need no of rows
# 	num_cols = len(table[0]) #all rows have same columns
# 	result = []   #accumulator for 1st loop

# 	for m in range (num_cols):
# 		row = []    #accumulator for 2nd loop
# 		for n in range(num_rows):
# 			row.append(table[n][m])  #create a new row list
# 		result.append(row)      #add result to table

# 	return result

# print(transpose(lst))

# lst = [[1, 2, 7], [3, 4, 8], [5, 6, 9]]

# def add_ones(table):
# 	"""
# 	Adds 1 to the every elements in the table
# 	Precon: table is a 2d list
# 	all table elements are int
# 	"""
# 	for rpos in range(len(table)):
# 		for cpos in range(len(table[rpos])):
# 			table[rpos][cpos] = table[rpos][cpos] + 1

# 	return table

# print(add_ones(lst))

# lst = [[1, 3, 5], [2, 4, 6]]

# def strip(table, col):
# 	"""Removes col from given table
# 	"""

# 	for rpos in table:
# 		rpos.pop(col - 1)

	
# 	# #walk thr the table
# 	# for rpos in range(len(table)):
# 	# 	#modify each row to slice out column
# 	# 	table[rpos] = table[rpos][:col] + table[rpos][col+1: ]
# strip(lst, 2)
# print(lst)


# d = {1:'shravan', 2:'shravan', 3:'lvs'}
# d1 = {2:'s', 3:'d', 4:'n'}

# d[1] = 'divpreet'
# print(d)

# del d[1]
# print(d)

# d[1] = 'divpreet'
# print(d)

# def max_grade(grade):
# 	"""
# 	Returns max grade is the grade dictionary
# 	Preco: grades has roll numbers as keys, ints as values
# 	"""
# 	# p = grade.values()
# 	# return max(p)

# 	maximum = 0         # Accumulator
# 	# loop over keys
# 	for k in grade:
# 		if grade[k] > maximum:
# 			maximum = grade[k]
# 	return maximum


# grade = {1:23, 2:24, 3:45, 4:12}
# # print(max_grade(grade))
# passed = []
# def roll_no_above_cutoff(grade, cutoff):
# 	"""Returns list of roll numbers with grades above or equal cutoff
# 	Pre: grades has roll nos as keys, ints as values, cutoff is an int."""

# 	global passed

# 	for k in grade:
# 		if grade[k] >= cutoff:
# 			passed.append(k)

# 	return passed

# print(roll_no_above_cutoff(grade, 23))

# def give_extra_credit(grades, rolls, bonus):
# 	""" Gives bonus points to everyone in sequens rolls

# 	Pre: grades have roll nos (rolls) as keys, int as values.
# 	rolls is a sequence of strings that are keys in grades
# 	bonus is an int"""
# 	for stds in grades:
# 		if stds in rolls:
# 			grades[stds] += bonus

# 	return grades

# print(give_extra_credit(grade, [2, 3], 7))