# Special Pythagorean triplet

# fsck it im just gonna brute force
for a in xrange(2, 1000):
	for b in xrange(a + 1, 1000):
		if a + b > 999:
			break
		for c in xrange(b + 1, 1000):
			total = a+b+c
			if total > 1000:
				break
			if total != 1000:
				continue
			if a**2 + b**2 == c**2:
				print a*b*c
				break