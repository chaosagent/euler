# Longest Collatz sequence

def collatz(n, counter=1):
	if n == 1: return counter
	counter += 1
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n+1
	return collatz(n, counter)

largest = 0
largestn = 0
for n in xrange(1, 1000000):
	terms = collatz(n)
	# print 'Number: %d, Terms: %d' % (n, terms)
	if terms > largest:
		largest = terms
		largestn = n

print largestn