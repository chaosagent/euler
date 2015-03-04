# Largest palindrome product
largest = 0
for x in xrange(999, 99, -1):
	for y in xrange(999, 99, -1):
		z = x*y
		if str(z) == str(z)[::-1]:
			if z > largest:
				largest = z
print largest