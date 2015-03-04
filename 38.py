# Pandigital multiples

pandigitalset = set(map(str, range(1,10)))

result = -1
for n in xrange(1,10000):
	# print n
	used = []
	i = 1
	while True:
		product = n * i
		isnotinused = len(set(list(str(product)))) == len(str(product))
		if isnotinused:
			for char in str(product):
				if char in used:
					isnotinused = False
					break
		if not isnotinused:
			if set(used) == set(pandigitalset):
				result = int(''.join(used))
			break
		used += str(product)
		i += 1
print result