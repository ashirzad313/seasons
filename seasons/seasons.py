import sys
import inflect
from datetime import date
from datetime import datetime

class Birth:
	def	__init__(self, year, month, day):

		self.year = year
		self.month = month
		self.day = day

	@property
	def year(self):
		return (self._year)
	@property
	def month(self):
		return (self._month)
	@property
	def day(self):
		return (self._day)
	@year.setter
	def	year(self, year):
		if not year:
			raise ValueError("Invalid year")
		if (ft_atoi(year) <= 0 or ft_atoi(year) > date.today().year):
			raise ValueError("Invalid year")
		self._year = ft_atoi(year)

	@month.setter
	def	month(self, month):
		if not month:
			raise ValueError("Invalid month")
		if (ft_atoi(month) <= 0 or ft_atoi(month) > 12):
			raise ValueError("Invalid month")
		elif (self._year == date.today().year and int(month) > date.today().month):
			raise ValueError("Invalid month")
		self._month = ft_atoi(month)
	@day.setter
	def	day(self, day):
		if not day:
			raise ValueError("Invalid day")
		if (ft_atoi(day) <= 0 or ft_atoi(day) > 31):
			raise ValueError("Invalid day")
		elif (self._year == date.today().year and self._month == date.today().month and int(day) > date.today().day):
			raise ValueError("Invalid day")
		self._day = ft_atoi(day)

	def	__str__(self):
		return (f"{self.year}-{self.month}-{self.day}")




def	main():
	array = get_birth()
	birth = Birth(array[0], array[1], array[2])
	output = get_output(birth)
	print(output)

def get_birth():
	date = input("Date of Birth: ").strip()
	if not date:
		raise ValueError("no empty str")
	array = date.split("-")
	if len(array) != 3:
		raise ValueError("Invalid format")
	return (array)

def get_output(birth):
	p = inflect.engine()
	date_time = datetime(birth.year, birth.month, birth.day)
	date_now = datetime.now()

	mnts = int(((date_now - date_time).days * (24 * 60)) + ((date_now - date_time).seconds / 60))
	output = p.number_to_words(mnts)
	return (output.replace(" and ", " "))

def ft_atoi(str):
	n = 0
	try:
		n = int(str)
	except:
		raise ValueError("Invalid date")
	return (n)



if __name__ == "__main__":
	main()
