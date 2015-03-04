# 10001st prime
import math
i = 0
x = 2
while True:
	isprime = True
	for j in xrange(2, int(math.sqrt(x)) + 1):
		if j != x and x % j == 0:
			isprime = False
			break
	if isprime:
		i += 1
		if i == 10001:
			print x
			break
	x += 1