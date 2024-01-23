def to_centi(n):
	'''return : x converted to centigrade
	
	'''
 assert type(n) == float, 'Precondition Violation'

	return 5*(n-32)/9.0
print(to_centi(73))
