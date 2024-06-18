def is_rctngle(x1,y1,x2,y2,x3,y3,x4,y4):
	'''
	Returns whether the quadrilateral made by the given points is a rectangle!

	this function is related to the confirmation of rectangle.
	
	parameters are related to the coordinate points os the vertices of the given geometry.
	parameters should be in a correct order.
	examples:

	'''

	if (x1==x2==x3==x4) or (y1==y2==y3==y4): #all
		return False
	elif x1==x2==x3 or x4==x2==x3 or x4==x1==x3 or x1==x2==x4 or y1==y2==y3 or y4==y2==y3 or y1==y4==y3 or y1==y2==y4:
		return False 
	elif (x1==x4 and x2==x3 and y1==y2 and y3==y4) or (x1==x2 and x4==x3 and y3==y2 and y1==y4):
		return True
	elif (((x3-x1)**2+(y3-y1)**2)**0.5) == (((x4-x2)**2+(y2-y4)**2)**0.5):

		if ((y3-y4)/(x3-x4))*((y1-y4)/(x1-x4)) == -1:
			return True
		else:
			return False



def is_inside():
	'''Tells whether the point is inside
	'''

	x1=float(input('enter the coordinate x1: '))
	y1=float(input('enter the coordinate y1: '))
	x2=float(input('enter the coordinate x2: '))
	y2=float(input('enter the coordinate y2: '))
	x3=float(input('enter the coordinate x3: '))
	y3=float(input('enter the coordinate y3: '))
	x4=float(input('enter the coordinate x4: '))
	y4=float(input('enter the coordinate y4: '))

	x=[x1,x2,x3,x4]
	y=[y1,y2,y3,y4]

	if is_rctngle(x1,y1,x2,y2,x3,y3,x4,y4):
		print("Graet, Your points are forming a rectangle \nNow give the points to be determined")

		x = float(input('Enter the x coordinate of the point: '))
		y = float(input('Enter the y coordinate of the point: '))

		ar_rect = abs(y3*(x1-x2) + y2*(x3-x1) + y1*(x2-x3))

		ar_trg1 = (1/2)*(abs(y*(x1-x2) + y2*(x-x1) + y1*(x2-x)))

		ar_trg2 = (1/2)*(abs(y3*(x4-x) + y*(x3-x4) + y4*(x-x3)))

		ar_trg3 = (1/2)*(abs(y3*(x-x2) + y2*(x3-x) + y*(x2-x3)))

		ar_trg4 = (1/2)*(abs(y4*(x1-x) + y*(x4-x1) + y1*(x-x4)))

		if ar_trg4==0 or ar_trg1==0 or ar_trg3==0 or ar_trg2==0:
			return "Your point is on the rectangle!"

		elif (ar_trg1 + ar_trg2 + ar_trg3 + ar_trg4) == (ar_rect) :

			return "The given point is inside of the rectangle"

		else:
			return "The given point is not inside the rectangle"

	else:
		return "Your points are not forming a rectangle"

print(is_inside())