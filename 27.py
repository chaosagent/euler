# Quadratic primes

from pyecm import fpf

primesunderthousand = []
primes = []
for n in xrange(2,10000):
	if len(fpf(n)) == 1:
		if n < 1000:
			primesunderthousand.append(n)
		primes.append(n)

largesta = -1001
largestb = -1
largest = 0
for a in xrange(-1000,1000):
	for b in primesunderthousand:
		n = 0
		while True:
			if not n**2 + a*n + b in primes:
				break
			n += 1
		if n > largest:
			largest = n
			largesta = a
			largestb = b
print largesta, largestb, largest, largesta*largestb