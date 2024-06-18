# def main():
# 	try:
# 		val = input('enter the number: ')
# 		x = float(val)
# 		print('the next number is' + str(x +1))
# 		assert x< 10, 'out pf range'
# 	except ValueError:
# 		print('Hey! That is not a number')
# 	# except AssertionError:
# 	# 	print('But, It is out of Bounds!')
# 	except:
# 		print('you are with me let\'s go')

# main()

# def foo(x):
# 	"""retruns the next number
# 	"""

# 	assert ttype(x)==int,'not an int'
# 	assert x <2, 'out of range'
# 	return x+1

# foo(3)

def foo(x):
	"""retruns the next number

	precondition: x is an int <2
	"""
	# assert ttype(x)==int,'not an int'
	if type(x) != int:
		msg = 'not an int'
		err = TypeError(msg)
		raise err
	# assert x <2, 'out of range'
	if x >= 2:
		msg = 'out of range'
		err = ValueError(msg)
		raise err
	
	return x+1

foo(3)