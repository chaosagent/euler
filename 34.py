# Digit factorials
from math import factorial as fact

results = []
for n in xrange(3,50000):
	if sum(map(fact,map(int,str(n)))) == n:
		results.append(n)

print sum(results)