class Time(object):
	"""Class represents time of the day.
	
	Att_hour: hour of the time
	INV: hour <= 23

	Att_min: min of the time
	INV: min < 59 
	"""
	def __init__(self, hour, minute):
		"""The time hour:minute
		Parameter hour: is hour component of time
		Precondition: hour is an int in 0 to 23

		Parameter minute: is minute component of time
		Precondition: minute is an int in 0 to 23
		"""
		assert type(hour) == int
		assert 0 <= hour and hour < 24
		assert type(minute) == int
		assert minute>=0 and minute<60

		self.hour = hour
		self.minute = minute


	def __str__(self):
		return '(' + str(self.hour) + ',' + str(self.minute) + ')'
	def __repr__(self):
		return str(self.__class__) + str(self)		


	def increament(self, hours, minutes):
		"""Move time hours and minutes into the                  future.

		Parameter_hours: is the hour component to be increased.
		Precondition: hours must be integer such that 0<=hours<=23 

		Parameter_minutes: is the minute component.
		precondition: minutes to be increased
		"""
		assert type(hours) == int
		assert type(minutes) == int
		assert hours > 0
		assert 0<=minutes and minutes <60

		self.minute = self.minute + minutes
		self.hour = self.hour + hours + (self.minute//60)
		
		self.hour = self.hour%24
		self.minute = self.minute%60

	def increament_t(self, t):
		"""Move time hours and minutes into the future.

		"""
		self.minute = self.minute + (t.minute)
		self.hour = self.hour + t.hour + (self.minute//60)
		
		self.hour = self.hour%24
		self.minute = self.minute%60

	def isPM(self):
		"""Returns True if noon or later"""
		return self.hour > 12