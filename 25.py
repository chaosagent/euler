# 1000-digit Fibonacci number

counter = 1
a=0
b=1
while True:
	a += b
	counter += 1
	if len(str(a)) >= 1000:
		print counter
		break
	a,b = b,a