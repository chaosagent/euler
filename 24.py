# Lexicographic permutations
from math import factorial as fact

def genperm(layer, n, target, available, current=0, perm=[]):
	print layer, current, perm, available, len(available)
	factorial = fact(len(available) - 1)
	print factorial
	for i in xrange(1, len(available) + 1):
		x = i * factorial + current
		print x
		if x >= target:
			perm.append(available[i - 1])
			del available[i-1]
		if x > target:
			current = x - factorial
			return genperm(layer + 1, n, target, available, current, perm)
		elif x == target:
			#reverse of available in order is last perm of this place
			return ''.join(perm + available[::-1])
#for x in range(1,7):
#	print genperm(0,list('012'), x, list('012'), 0, [])
print genperm(0, ['0','1','2','3','4','5','6','7','8','9'], 1000000, ['0','1','2','3','4','5','6','7','8','9'])