# Pandigital products

from copy import deepcopy as cp

numbers = range(1,10)

works = []
def test(chain):
	if len(chain) == 5:
		number1, number2 = int(''.join(chain[:2])), int(''.join(chain[2:]))
		product = number1 * number2
		if len(chain + list(str(product))) == 9 and set(map(int, chain + list(str(product)))) == set(numbers) and product not in works:
			# print number1, number2, product
			works.append(product)
		number1, number2 = int(''.join(chain[:1])), int(''.join(chain[1:]))
		product = number1 * number2
		if len(chain + list(str(product))) == 9 and set(map(int, chain + list(str(product)))) == set(numbers) and product not in works:
			# print number1, number2, product
			works.append(product)
		return
	for n in numbers:
		if n not in chain:
			newchain = cp(chain)
			newchain.append(str(n))
			test(newchain)
test([])

print sum(works)