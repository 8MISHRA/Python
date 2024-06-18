# def fibbonacci(n):
# 	"""
# 	Returns a fibbonacci series of n terms

# 	A series is in which next term is the sum of previous two terms
# 	is called fibbonacci series

# 	Parameter_n: n is the number of terms in the series
# 	Precondition: n is int and n > 0

# 	Examples:

# 	>>> fibbonacci(1)
# 	[0]
# 	>>> fibbonacci(2)
# 	[0,1]
# 	>>> fibbonacci(3)
# 	[0,1,1]
# 	>>> fibbonacci(4)
# 	[0,1,1,2]
# 	>>> fibbonacci(5)
# 	[0,1,1,2,3]
# 	>>> fibbonacci(6)
# 	[0,1,1,2,3,5]
# 	"""
# 	result = []
# 	for i in range(n):
# 		if i == 0:
# 			result = [0]

# 		if i == 1:
# 			result = [0,1]

# 		if i > 1:
# 			p = result[i - 1] + result [i - 2]
# 			result.append (result[i - 1] + result [i - 2])

# 	return (result)

# n = int(input('Enter no. of terms of ur fibonacci series: '))
# print(fibbonacci(n))


# class A:
# 	def __init__(self):
# 		self.a = 'Old'
# 		self.change(self.a)
# 	def change(self, value):
# 		value = 'New'

# obj = A()
# print(obj.a)

class A:
	def __init__(self):
		self.a = 'I m a'
class B(A):
	# def __init__(self):
	print(self.a)

obj = B()