from pyecm import isprime

n = 11
truncprimes = []
count = 0
while count < 11:
	wstring = ''
	works = True
	for number in str(n):
		wstring += number
		if not isprime(int(wstring)):
			works = False
			break
	if not works:
		n += 1
		continue
	wstring = ''
	for number in str(n)[::-1]:
		wstring = number + wstring
		if not isprime(int(wstring)):
			works = False
			break
	if not works:
		n += 1
		continue
	truncprimes.append(n)
	count += 1
	n += 1
print sum(truncprimes)