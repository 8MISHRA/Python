class Time(object):
	"""Class represents time of the day.
	"""

	# Att_hour: hour of the time
	# INV: hour <= 23

	# Att_min: min of the time
	# INV: min < 59 
	def _is_minute(self, m):         # It is hidden method and will not be displayed when the class is called by the help
		return (type(m) == int and 0 <= m <60)

	def getHour(self, h):
		return self._hour

	def setHour(self, h):
		assert type(h) == int
		assert 0 <= h < 24
		self._hour = h


	def __init__ (self, hour, minute ):
		"""The time hour:minute
		Parameter hour: is hour component of time
		Precondition: hour is an int in 0 to 23

		Parameter minute: is minute component of time
		Precondition: minute is an int in 0 to 23
		"""
		assert type ( _hour ) == int
		assert 0 <= _hour < 24
		assert type(minute) == int
		assert 0 <= minute < 60

		self._hour = hour
		self._minute = minute


	def __str__ (self):
		return '(' + str(self._hour) + ',' + str(self.minute) + ')'
	def __repr__(self):
		return str(self.__class__) + str(self)		


	def increament(self, hours, minutes):
		"""Move time hours and minutes into the future.

		Parameter_hours: is the hour component to be increased.
		Precondition: hours must be integer such that 0<=hours<=23 

		Parameter_minutes: is the minute component.
		precondition: minutes to be increased
		"""
		assert type(hours) == int
		assert type(minutes) == int
		assert hours > 0
		assert 0 <= minutes and minutes < 60

		self._minute = self._minute + minutes
		self._hour = self._hour + hours + (self._minute//60)
		
		self._hour = self._hour%24
		self._minute = self._minute%60

	def increament_t(self, t):
		"""Move time hours and minutes into the future.

		"""
		self._minute = self._minute + (t.minute)
		self._hour = self._hour + t._hour + (self._minute//60)
		
		self._hour = self._hour%24
		self._minute = self._minute%60

	def isPM(self):
		"""Returns True if noon or later"""
		return self._hour >= 12