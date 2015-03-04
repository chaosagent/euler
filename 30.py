# Digit fifth powers

works = []
for n in xrange(2,1000001):
	if sum(map(lambda x: x**5,map(int, str(n)))) == n:
		works.append(n)
print sum(works)