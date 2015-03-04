# Circular primes
from pyecm import fpf
from itertools import combinations as comb

def isprime(n):
	return len(fpf(n)) == 1
def listrotates(l):
	toreturn = []
	for i in xrange(len(l)):
		toreturn.append(l[i:] + l[:i])
	return toreturn
count = 0
for n in xrange(2, 1000001):
	works = True
	for n2 in listrotates(str(n)):
		if not isprime(int(''.join(n2))):
			works = False
			break
	if works:
		#print n
		count += 1
print count