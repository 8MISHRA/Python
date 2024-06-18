def add_one(input):
	"""
	Generates 1 added to every element of input

	Example: If data is 1,2,3,1 then this generator
	iterates 2,3,4,2

	Parameter input: The data to process
	Precondition: input an iterable, each element an int
	"""

	for x in input:
		yield x+1

def evens(input):
	"""
	Generates only the elements of data that are even.

	Example: If data is 0, 1, 2, 3, 4, then this generator
	iterates 0, 2, 4

	Parameter input: The data to process
	Precondition: input an iterable, each element an int
	"""
	for x in input:
		if x%2 == 0:
			yield x

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

