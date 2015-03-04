# Pandigital prime

from pyecm import isprime
from copy import deepcopy as cp

result = 0
def test(sequence):
	if len(sequence) == 7:
		if isprime(int(''.join(map(str,sequence)))):
			global result
			result = int(''.join(map(str,sequence)))
		return
	for n in xrange(1,8):
		if not n in sequence:
			sendsequence = cp(sequence)
			sendsequence.append(n)
			test(sendsequence)

test([])
print result