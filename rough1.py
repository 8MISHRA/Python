'''def swap(b, h, k):
	"""swaps b[h] and b[k] in b

	precond:b is a mutable list,
	h,k are valid positions"""

	temp = b[h]
	b[h] = b[k]
	b[k] = temp

x = [5,4,7,3,8]
swap(x, 3, 4)

#isko khud se bnao yrr'''

def print_each(text):
	"""Prints each char of text
	Pre:text is a string"""

	for x in text:
		print(x)

print_each('ab')