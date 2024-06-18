def count_word(first_str, second_str, query_word):

	"""Compares the repeatation of the given wod in the given strings

	Counts the number of the given word in the string
	and compare them then
	prints which one has more repeatation 'First', 'Second', or 'Both' have 
	equal number of repeatation

	Parameter_first_str: This is the first string given
	Precondition: This should be of sring type

	Parameter_second_str: This is the second string given
	Precondition: This should be of sring type

	Parameter_query_word: This is the word given to compare
	Precondition: This should be of sring type

	"""
	no_first_str = (first_str.split()).count(query_word) #counts the number of the given word in first string
	no_second_str = (second_str.split()).count(query_word) #counts the number of the given word in second string

	if no_first_str > no_second_str:
		print('First')
	
	elif no_first_str < no_second_str:
		print('Second')
	
	else:
		print('Both')

first_str = input ("Enter your first string: ").lower()
second_str = input("Enter your second string: ").lower()
query_word = input ("The word that you want to count: ").lower()

count_word (first_str, second_str, query_word)