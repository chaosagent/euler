# Prime permutations

from pyecm import fpf
from itertools import combinations as comb

def findsums(diffs, wdiffs=[], l=1):
	if l == len(diffs):
		return wdiffs
	for i in xrange(len(diffs) - l):
		wdiffs.append(sum(diffs[i:i+l+1]))
	return findsums(diffs,wdiffs,l + 1)

primes = []
for n in xrange(1000,10000):
	if len(fpf(n)) == 1:
		primes.append(n)
primesets = map(set,map(str,primes))
# print primes
workingsets = []
for prime in primes:
	primeset = set(str(prime))
	permprimes = []
	indices = []
	for i in xrange(len(primesets)):
		if primeset == primesets[i]:
			indices.append(i)
			permprimes.append(primes[i])
	for x in comb(permprimes,3):
		if x[1] - x[0] == x[2] - x[1]:
			if x not in workingsets:
				workingsets.append(x)

print ''.join(map(str,workingsets[1]))
"""
	primedifferences = []
	for i in xrange(len(permprimes) - 1):
		primedifferences.append(permprimes[i+1] - permprimes[i])
	if len(indices) < 3:
		continue
	primediffs = findsums(primedifferences,[],1)
	if prime == 1487: print primedifferences
	if prime == 1487: print primediffs
	occ = {}
	for i in xrange(len(primediffs)):
		if not primediffs[i] in occ:
			occ[primediffs[i]] = []
		occ[primediffs[i]].append(i)
	if prime == 1487: print occ
	for key,values in occ.iteritems():
		if len(values) >= 3:
			print primedifferences, primediffs, occ, key, values
			exit()"""