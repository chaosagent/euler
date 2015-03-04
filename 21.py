# Amicable numbers
from pyecm import fpd

amicables = []
sums = {}
for n in xrange(2,10001):
	spd = sum(fpd(n))
	if not spd in sums:
		sums[spd] = [n]
	else:
		sums[spd].append(n)
# print sums
for key,values in sums.iteritems():
	for x in values:
		if key == x or not x in sums:
			continue
		if key in sums[x]:
			if key not in amicables:
				amicables.append(key)
			if x not in amicables:
				amicables.append(x)
# print amicables
print sum(amicables)