"""Datetime class for timestamps"""

__author__ = "Yun Chang"
__email__ = "yunchang@mit.edu"

SEC2NSEC = 1e9 
MIN2SEC = 60
HR2MIN = 60 
DAY2HR = 24

class Datetime: 
	def __init__(self, string):
		self.year = 0
		self.month = 0
		self.day = 0
		self.hr = 0
		self.min = 0
		self.sec = 0
		self.nanosecs = 0

		# initiate from a line in KittiFile 
		# ex: 2011-09-26 13:02:25.594360375
		[date, time] = string.split()
		[year_str, month_str, day_str] = date.split("-")
		[hr_str, min_str, sec_str] = time.split(":")
		[secs_str, nsecs_str] = sec_str.split(".")

		self.year = float(year_str)
		self.month = float(month_str)
		self.day = float(day_str)

		self.hr = float(hr_str)
		self.min = float(min_str)
		self.sec = float(secs_str)
		self.nanosecs = float(nsecs_str)

	def toSeconds(self):
		# discard the years and months and days and convert to seconds 
		hr2sec = self.hr*HR2MIN*MIN2SEC
		min2sec = self.min*MIN2SEC
		nsec2sec = self.nanosecs/SEC2NSEC
		return hr2sec + min2sec + self.sec + nsec2sec

	def toNanoseconds(self):
		sec = toSeconds
		return sec * 1e9

	def __eq__(self, other):
		return (self.year == other.year and 
						self.month == other.month and 
						self.day == other.day and
						self.hr == other.hr and 
						self.min == other.min and 
						self.sec == other.sec and 
						self.nanosecs == other.nanosecs)

	def __gt__(self, other):
		if self.year < other.year:
			return False
		elif self.year > other.year:
			return True 
		else: 
			if self.month < other.month:
				return False
			elif self.month > other.month:
				return True 
			else:
				if self.day < other.day:
					return False
				elif self.day > other.day:
					return True  
				else:
					return (self.toSeconds() > other.toSeconds())

	def __ge__(self, other):
		return (self == other or self > other)

	def __lt__(self, other):
		return (other > self)

	def __le__(self, other):
		return (other > self or other == self)
