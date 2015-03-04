# Non-abundant sums
from pyecm import fpd

abundants = []
for n in xrange(2,28124):
	if sum(fpd(n)) > n:
		abundants.append(n)
#print abundants
#print len(abundants)

abundantset = set(abundants)

total = 0
for n in xrange(1,28124):
	issum = False
	for x in abundants:
		if x >= n:
			break
		if n - x in abundantset:
			issum = True
			break
	if not issum:
		# print '%d is not a sum!' % n
		total += n
print total