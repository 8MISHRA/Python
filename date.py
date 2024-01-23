def isleapyear(year):
	"""Returns True if y is a leap year. False otherwise
	Precondition: y is an int >= 0"""

	assert type(year) == int
	assert year>=0
	if year%4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return True
	else:
		return False


class Date(object):
	"""A class representing a month, day and year
	Attribute MONTHS: A CLASS ATTRIBUTE list of all month abbreviations in order
	Attribute DAYS: A CLASS ATTRIBUTE that is a dictionary. Keys are the strings from MONTHS; values are days in that month ('Feb' is 28 days)"""
	# Attribute _year: The represented year. An int >= 2000 (IMMUTABLE)
	# Attribute _month: The month. A valid 3-letter string from MONTHS (IMMUTABLE)
	# Attribute _day: The day. An int representing a valid day of _month (MUTABLE)

	MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month_dict = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED

	def getYear(self):
		"""Returns the year of this date"""
		return self._year
	

	def  getMonth(self):
		"""Returns the month of this date"""
		return self._month


	def getDay(self):
		"""Returns the day of this date"""

		return self._day
	
	def setDay(self,d):
		"""Sets the day of this date
		Parameter value: The new day
		Precondition: value is a valid day in the month"""
		# Fill in missing part

		assert type(d) == int
		assert d>=0
		if self._month in ['Jan','Mar','May','Jul','Aug','Oct','Dec']:
			assert d<=31
		elif self._month in ['Apr','Jun','Sep','Nov']:
			assert d<=30
		elif isleapyear(self._year):
			assert d<=29
		else:
			assert d<=28

		self._day = d

	def __init__(self, y, m ,d):  
		# Fill in missing part
		"""Initializes a new date for the given month, day, and year

		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month

		Precondition: d is an int and a valid day for month m"""
		# Fill in missing part

		MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

		assert type(y) == int , 'Year should be integer'
		assert y >= 2000, 'Year is out of range'
		assert type(m) == str, 'Month should be a non empty string'
		assert m in MONTHS, 'Month name should be its first three letters with first letter in uppar case'

		self._month = m
		self._year = y
		self.setDay(d)


	def __str__(self):
		"""Returns string with clear contents
		"""
		return self._month + ' ' + str(self._day) +', ' + str(self._year) 

	def __lt__(self, other):
		"""Returns True if this date happened before other (False otherwise)

		Precondition: other is a Date

		This method causes a TypeError if the precondition is violated."""

		MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

		if not (isinstance(other, Date)):
			message = 'This date is not a Date object'
			error = TypeError(message)
			raise error

		return self._year < other._year or ((self._year == other._year)and(MONTHS.index(self._month) < MONTHS.index(self._month)) 
			or((MONTHS.index(self._month) == MONTHS.index(self._month)) and (self.getDay() < other.getDay())))


		# IMPORTANT: You are limited to 20 lines. Do NOT brute force this.

class DateTime(Date):
	"""A class representing a month, day and year, plus time of day (hours, minutes)"""
	# Attribute _hour: The hour of the day. An int in range 0..23 (MUTABLE)
	# Attribute _minute: The minute of the hour. An int in range 0..59 (MUTABLE)

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.

	def getHour(self):
		"""Returns the hour of the day"""
		return self._hour

	def setHour(self, value):
		"""Sets the hour of the day
		Parameter value: The new hour
		Precondition: hour is an int in 0..23"""

		assert type(value) == int,'Hour should be integer'
		assert 0<=value<=23, 'Hour value is out of range'

		self._hour = value

	def getMinute(self):
		"""Returns the minute of the hour"""
		return self._minute

	def setMinute(self, value):
		"""Sets the hour of the day
		Parameter value: The new hour
		Precondition: hour is an int in 0..59"""

		assert type(value) == int, 'Minute should be integer'
		assert 0<=value<=59
		self._minute = value

	def __init__(self, y, m, d, h=0, minute=0):
		"""Initializes a new datetime for the given month, day, year, hour and minute
		This method adds two additional (default) parameters to the initialize for
		Date. They are hr (for hour) and mn (for minute).
		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month
		Precondition: d is an int and a valid day for month m
		Precondition: hr is an int in the range 0..23 (OPTIONAL; default 0)
		Precondition: mn is an int in the range 0..59 (OPTIONAL; default 0)"""

		super().__init__(y, m, d)
		self.setHour(h)
		self.setMinute(minute)

	def __str__(self): # Fill in missing part
		"""Returns a string representation of this DateTime object
		The representation is 'hh:mm on month day, year' like this: '9:45 on Jan 2, 2002'
		Single digit minutes should be padded with 0s. Hours do not need to be padded."""

		if self._minute < 10:
			return str(self._hour) + ':0' + str(self._minute) +' on ' + super().__str__()
		return str(self._hour) + ':' + str(self._minute) +' on ' + super().__str__()