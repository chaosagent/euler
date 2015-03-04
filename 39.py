# Integer right triangles

from math import sqrt

count = {}

for a in xrange(1,1000):
	a = float(a)
	for b in xrange(1,1000):
		b = float(b)
		c = sqrt(a**2 + b**2)
		p = int(a + b + c)
		if p > 1000:
			break
		if not c % 1 == 0:
			continue
		if not p in count:
			count[p] = 0
		count[p] += 1
largest = -1
largestkey = -1
for number, value in count.items():
	if value > largest:
		largest = value
		largestkey = number
print largestkey