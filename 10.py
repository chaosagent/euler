# Summation of primes
import math
total = 0
for i in xrange(2, 2000000):
	isprime = True
	for j in xrange(2, int(math.sqrt(i)) + 1):
		if j != i and i % j == 0:
			isprime = False
			break
	if isprime:
		total += i
print total