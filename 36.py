# Double-base palindromes

def palindromic(s):
	return s == s[::-1]
total = 0
for n in xrange(1,1000000):
	if palindromic(str(n)) and palindromic(bin(n)[2:]):
		print '%d | %s is palindromic! Total: %d' % (n,bin(n)[2:],total)
		total += n
print total