# try:
# 	result = input('Number: ')
# 	s = float(result)
# 	print('The next no. is '+ str(s +1))
# except:
# 	print('That is not a number! Try again')
# 	result = input('Number: ')
# 	x = float(result)
# 	print('The next number is '+str(x+1))

# loop = True
# while loop:
# 	try:
# 		result = input('Number: ')
# 		s = float(result)
# 		print('The next no. is '+ str(s +1))
# 		loop = False
# 	except:
# 		print('That is not a number! Try again')

# def sum_square(n):
# 	"""Rets: sum of squares from 1 to n-1
# 	Prec: n is int > o
# 	"""
# 	print('Before while')
# 	total = 0           # accumulator
# 	# for x in range(n):
# 	# 	total = total + x*x
# 	# return (total)
# 	x = 0               # accumulator
# 	while x<n:
		
# 		print('Start loop '+str(x))
# 		total = total + x*x
# 		# x = x+1
# 		print('End loop')
# 	print('After while')

# print(sum_square(5))

# def count_slash(s):
"""Returns the no of times '/' appears in s,

	Parameter s: the string to search
	Precondition: s is a possibly empty string
	"""
	# count_sl = 0
	# for i in range(len(s)):
	# 	if s[i] == '/':

	# 		count_sl += 1
	# return count_sl

	# i = 0   # loop var
	# while i < len(s):

	# 	if s[i] == '/':
			
	# 		count_sl += 1

	# 	i += 1 # loop var increase
	# while i in [s]:
	# 	if i == '/':

	# 		count_sl += 1

	# 	i += 1
# 	return count_sl

# print(count_slash('g////abcd'))

# def add_fracs(n):
# 	"""Returns: the sum of fraction 1/1 + 1/2 + 1/3 + ... + 1/n

# 	Parameter n: the number of fractions to add
# 	Precondition: n is an int > 0 
# 	"""
# 	v = 0 
# 	# for i in range(1, n+1):
# 	# 	v = v + (1.0/i)

# 	# return v 

# 	p = 1

# 	while p <= n:
# 		v = v + (1.0/p)
# 		p += 1
# 	return v

# print(add_fracs(10))
# valid = ('s', 't', 'a', 'r', 'e')
# prmpt= 'Enter your choice'
# def prompt(prmpt, valid):

# 	response = input(prmpt)
# 	# for i in valid:
# 	# 	if prompt == i:
# 	# 		return prompt
# 	i = 0
# 	while not (response in valid):
# 		print('Invalid response. Answer must be one of ' + str(valid))
# 		response = input(prmpt)

# 	return response
		
	

# print(prompt(prmpt, valid))
# import random
# def roll_pass(goal):
# 	'''Returns: the score from rolling a die untill passing goal.
# 	This function starts with score of 0, and rolls die, adding the result to the score. Once the score passes goal
# 	it stops and returns the result as the final score.
# 	if the function ever rolls a 1, it stops and returns 0
# 	'''
# 	# import random
# 	loop = True
# 	score = 0
# 	while loop:
# 		die_roll = random.randint(1, 6)
# 		print(die_roll)
# 		if die_roll == 1:
# 			score = 0
# 			loop = False
# 		else:
# 			score += die_roll
# 			loop = score < goal

# 	return score 

# print(roll_pass(55))

# def list_squares(n):
# 	'''Returns a list of all squares less than n

# 	Example: list_squares(10) returns [0, 1, 4, 9]
# 	'''
# 	squrs = []
# 	# for i in range(int(n**0.5) + 1):
# 	# 	squrs.append(i*i)

# 	k = 0
# 	while k*k < n:
# 		squrs.append(k*k)
# 		k += 1
# 	return squrs


# print(list_squares(18))  

# fib = [1, 1]
# # for k in range(2, 10):
# # 	fib.append(fib[-1] + fib[-2])

# while len(fib) < 10:
# 	fib.append(fib[-1] + fib[-2])
# print(fib)

# def rem3(lst):
# 	'''removes all 3s from the lst'''

# 	while 3 in lst:
# 		lst.remove(3)
# 	# i = 0
# 	# while i < len(lst):
# 	# 	#no of 3's in lst[0...i-1]
# 	# 	if lst[i] == 3:
# 	# 		del lst[i]
# 	# 	else:
# 	# 		i += 1


# lst = [1, 3, 3, 2, 3, 4, 33]

# rem3(lst)
# print(lst)

# threshold = 1e-6
# def sqrut(n):
# 	x = n/2
	
# 	while abs(x*x - n) > 1e-06:
# 		x = x/2 + n/(2*x)

# 	return x
# import math
# p = math.sqrt(2)
# print(p)

# print(sqrut(2))


l=[4, 4, 'a', 'b', 10]

def sum_ele(l):
    if len(l)==0:
        return 0
    try:
        if type(l[0]) in [int, float]:
            left=l[0]
            right=sum_ele(l[1:])
        else:
            right=sum_ele(l[1:])
        return left + right
    except:
        print('error_')
print(sum_ele(l))



