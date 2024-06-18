"""
A module showing off some classic for-loops

This module is for comparison with gens.py
This module shows the old way of doing things
"""

def add_one(input):
	"""
	Returns the list with 1 added to every element of input
	
	Example: add_one([1,2,3,1]) returns [2,3,4,2]

	Parameter input: The data to process
	Precondition: input is an iterable, each element an int
	"""
	copy = []
	for x in input:
		x = x+1
		copy.append(x)
	return copy


def evens(input):
	"""
	Returns a list with only the even elements of data

	Example: evens([0, 1, 2, 3, 4]) returns [0, 2, 4]

	Parameter input: The data to process
	Precondition: input an iterable, each element an int
	"""
	result = []
	for x in input:
		if x%2 == 0:
			result.append(x)
	return result

def average(input):
    """Returns a list with a running average of input
    
    The running average is a list with the same size
    as the input. Eacch element at position n is the
    average of all of the elements in input[:n+1]

    Ex: average([1, 3, 5, 7]) returns [1.0, 2.0, 3.0, 4.0]
    
    Parameter input: The data to process
    Precond: input an iterable, each element a number"""
    
    result = []  # actual accumulator    
    sum = 0      # accumulator “helper”
    count = 0    # accumulator “helper”
    for x in input:
        sum = sum+x
        count = count+1
        result.append(sum/count)
    return result
