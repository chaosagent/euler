# Highly divisible triangular number
from pyecm import ff

x = 1
i = 2
while True:
	x += i
	i += 1
	factors = len(ff(x))
	# print 'Number: %d, Factors: %d' % (x,factors)
	if factors > 500:
		print x
		break