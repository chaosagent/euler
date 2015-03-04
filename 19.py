# Counting Sundays

def getDays(month, year):
	if month in [3,5,8,10]:
		return 30
	elif month == 1:
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			return 29
		else:
			return 28
	else:
		return 31

tyears = 100
tmonths = tyears * 12
# start at jan 1, 1901
day = 2
year = 1901
count = 0
for month in xrange(tmonths):
	if month != 0 and month % 12 == 0:
		year += 1
	# print 'Year: %d, Month: %d, Day: %d' % (year, month % 12, day + 1)
	if day == 0:
		count += 1
		# print 'Month %d has Sunday 1st' % (month % 12 + 1)
	day += getDays(month%12, year)
	day = day % 7
print count