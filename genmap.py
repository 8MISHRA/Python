"""
A module reimagining map and filter generators
"""

def map(f,data):
	"""
	Generates f applied to each element of data

	Parameter f: The function to apply
	Precondition: f is a function taking exactly one argument

	Parameter data: The data to process
	Precondition: data an iterable, each element satisfying p
	"""
	for item in data:
		yield(item)


def filter(f,data):
	"""
	Generates only the elements of data for which f is True

    Parameter f: The function to apply
    Precondition: f is a boolean function taking exactly one 
    
    Parameter data: The data to process
    Precondition: data an iterable, each element satisfying p
    """
	for item in data:
		if f(item):
			yield item


def plus1(x):
    """
    Returns x+1

    Parameter x: the umber to add to
    Precondition: x is an int or float
    """
    return x+1


def negate(x):
    """
    Returns -x

    Parameter x: The number to negate
    Precondition: x is an int or float
    """
    return -x


def iseven(x):
	"""
	Returns True if x is even

	Parameter x: The number to add to
	Precondition: x is an int
	"""

	return x % 2 == 0


def ispos(x):
	"""
	Returns True if x > 0

	Parameter x: The number to add to
	Precondition: x is an int or float
	"""
	return x > 0

def averages(input):
	"""
	Generates a running average of input

	The running average is an iterator the same size
	as the input. Each element is the average of all
	of the elements in the input so far.

	Example: If data is 1, 3, 5, 7 then this generator
	iterates 1.0, 2.0, 3.0, 4.0

	Parameter input: The data to process
	Precondition: input an iterable, each element a number
	"""
	sum = 0
	count = 0
	for x in input:
		sum += x
		count += 1
		yield sum/count

