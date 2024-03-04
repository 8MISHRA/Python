# Receiving required data from the user

old=input('Enter original currency: ')
new=input('Enter desired currency: ')
amt=float(input('Enter original amount: '))

import Divyansh_a1

if (not(Divyansh_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()

# if the target currency is not valid, quit
if(not(Divyansh_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()

Divyansh_a1.exchange(old,new,amt)

