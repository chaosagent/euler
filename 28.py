# Number spiral diagonals

result = 1
n = 1
increment = 0
for i in xrange(500):
	increment += 2
	for i in xrange(4):
		n += increment
		result += n
print result