# Digit cancelling fractions
from fractions import gcd as gcf

def mult(ns):
	r = 1
	for x in ns:
		r *= x
	return r

numerators = []
denominators = []
for x in xrange(10,100):
	x = str(x)
	for y in xrange(int(x)+1,100):
		y = str(y)
		if x[1] == '0' and y[1] == '0':
			continue
		wx, oy = x, y
		origvalue = float(wx)/float(y)
		union = list(set(wx) & set(y))
		if len(union) == 1:
			wx = wx.replace(union[0], '', 1)
			y = y.replace(union[0], '', 1)
		else:
			continue
		try:
			if origvalue == float(wx)/float(y):
				numerators.append(int(x))
				denominators.append(int(oy))
				# print x,oy
		except:
			pass
# print numerators, denominators
numerator = mult(numerators)
denominator = mult(denominators)
# print numerator, denominator
divisor = gcf(numerator, denominator)
numerator /= divisor
denominator /= divisor
print denominator

