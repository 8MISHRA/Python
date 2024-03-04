"""
	Module for currency exchange
	This module provides several string parsing functions to
	implement a
	simple currency exchange routine using an online currency
	service.
	The primary function in this module is exchange.
	Author: DIVYANSH MISHRA
	Date: 30/11/2022
"""

def before_space(s):
	'''Returns a copy of s up to, but not including, the first space
	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	examples:
	>>> before_space('usd doller')  #noraml case
	'usd'
	>>> before_space("  indian    rupee  ")  #having spaces at the both ends
	'indian'
	'''
	p=s.strip()
	return p[:p.find(' ')].strip()

def after_space(s):
	'''Returns a copy of s after the first space
	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	Implement these functions according to their specification. In other words
	examples:
	>>> after_space('usd doller')  #normal test
	'doller'
	>>> after_space('usd   doller')  #having more than one space
	'doller'
	>>> after_space('  usd   doller  ')  #having spaces at the both ends
	'doller'
	'''	
	p=s.strip()
	return p[(p.find(' ')):].strip()

def first_inside_quotes(s):
	'''Returns the first substring of s between two (double) quotes
	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of
	it.
	Examples:
	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C' 
	because it only picks the first such substring
	Parameter s: a string to search
	Precondition: s is a string containing at least two double
	quotes
	example:
	>>> first_inside_quotes('A "B C" D')  #normal test
	'B C'
	>>> first_inside_quotes('A "B C" D "E F" G')   #having more than one (") 
	'B C'
	'''
	return s[(s.find('"'))+1:(s[(s.find('"'))+1:].find('"'))+(s.find('"'))+1].strip()

def get_lhs(json):
	'''Returns the lhs value in the response to a currency query
	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword
	"lhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON response
	contains an error message.
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	example:
	>>> get_lhs('{"lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')  #normal test
	'1 Bitcoin'
	>>> get_lhs('{"lhs" : "1 usd", "rhs" : "19995.85429186 Euros", "err" : "" }')  #having otheer currency
	'1 usd'
	>>> get_lhs('{ "lhs" : "", "rhs" : "19995.85429186 Euros", "err" : ""}')  #having no value of lhs
	''
	'''
	return json[json.find(':')+3:json.find('",')]


def get_rhs(json):
	'''Returns the rhs value in the response to a currency query
	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword
	"rhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not
	'"38781.518240835 Euros"').
	This function returns the empty string if the JSON response
	contains an error message.
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	examples:
	>>> get_rhs('{"lhs":"1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')  #normal case
	'19995.85429186 Euros'
	>>> get_rhs('{"lhs":"abc", "rhs" : "19995.85429186 Euros", "err" : "currecny is not valid" }')  #having invalid currency with error
	'19995.85429186 Euros'
	>>> get_rhs('{"lhs":"", "rhs" : "19995.85429186 Euros", "err" : "currecny is not valid" }')  #not having any lhs value
	'19995.85429186 Euros'
	>>> get_rhs('{"lhs":"", "rhs" : "1999 Euros", "err" : "" }')  #having integral rhs
	'1999 Euros'
	'''
	
	return (json[json.find('rhs')+8:])[:(json[json.find('rhs')+8:]).find('"')]

def has_error(json):
	'''Returns True if the query has an error; False otherwise.
	Given a JSON response to a currency query, this returns True if
	there
	is an error message. For example, if the JSON is
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It
	does NOT return the message 'Currency amount is invalid.').
	Parameter json: a json string to parse
	Precondition: json is the response to a currency
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }')  #normal test
	True
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "" }')  #having no error
	False
	'''
	strt=json.find('"err"')
	end=json.find('"}')
	
	return bool(json[strt+9:end-2])


def query_website(old, new, amt):
	'''Returns a JSON string that is a response to a currency query.
	A currency query converts amt money in currency old to the
	currency new. The response should be a string of the form
	'{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
	where the values old-amount and new-amount contain the value
	and name for the old and new currencies. If the query is
	invalid, both old-amount and new-amount will be empty, while
	"err" will have an error message.
	Parameter old: the currency on hand
	Precondition: old is a string with no spaces or non-letters
	Parameter new: the currency to convert to
	Precondition: new is a string with no spaces or non-letters
	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	examples:
	#normal case
	>>> query_website('USD','INR',100)
	'{ "lhs" : "100 United States Dollars", "rhs" : "7978.8013 Indian Rupees", "err" : "" }' #normal test
	>>> query_website('inr','cup',12)
	'{ "lhs" : "12 Indian Rupees", "rhs" : "3.8727621904809 Cuban Pesos", "err" : "" }'  #test with small letters
	>>> query_website('aaa','cup',12)
	'{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }'  #having invalid currency code
	'''
	import requests
	od=old.upper()
	nw=new.upper()
	json = (requests.get(f'http://cs1110.cs.cornell.edu/2022fa/a1?old={od}&new={nw}&amt={amt}')).text
	return json

def is_currency(code):
	'''Returns: True if code is a valid (3 letter code for a) currency
	It returns False otherwise.
	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters.
	examples:
	>>> is_currency('INR')  #normal test
	True
	>>> is_currency('usd')  #test for lower case
	True
	>>> is_currency('UsD') #test for mixup of upper and lower case
	True
	>>> is_currency('abC')  #test for invalid currency
	False
	'''
	cod = code.upper()
	json = query_website(cod,cod,1.0)
	return not(has_error(json))


def exchange(old, new, amt):

	"""
	Returns the amount of currency received in the given
	exchange. In this exchange, the user is changing amt money in
	currency old to the currency new. The value returned represents
	the amount in currency new.
	The value returned has type float.
	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code
	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code
	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	examples:
	>>> exchange('USD', 'INR', 10)  #norrmal test
	'797.88013 Indian Rupees'
	>>> exchange('usd', 'inr', 10 )  #with lower case
	'797.88013 Indian Rupees'
	>>> exchange('BTC', 'USD', 10)  #some other currency
	'198549.24041017 United States Dollars'
	>>> exchange('SBG', 'USD', 10)  #invalid currency
	''
	
	"""

	p = query_website(old, new, amt)
	o = old.upper()
	q = get_rhs(p) 
	r = before_space(q)
	n = new.upper()
	print(f'You can exchange {amt} {o} for {r} {n}')
	