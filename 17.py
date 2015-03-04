# Number letter counts

def onesletters(n):
	n = int(n)
	return {
		1: 3,
		2: 3,
		3: 5,
		4: 4,
		5: 4,
		6: 3,
		7: 5,
		8: 5,
		9: 4,
		0: 0
	}[n]

def tensletters(n):
	n = int(n)
	return {
		10: 3,
		11: 6,
		12: 6,
		13: 8,
		14: 8,
		15: 7,
		16: 7,
		17: 9,
		18: 8,
		19: 8
	}[n]
def twentiesletters(n):
	n = int(n)
	return {
		2: 6,
		3: 6,
		4: 5,
		5: 5,
		6: 5,
		7: 7,
		8: 6,
		9: 6,
		0: 0
	}[n]
result = 0
for x in range(1,1001):
	n = str(x)
	if x % 100 >= 10 and x % 100 < 20:
		result += tensletters(n[-2] + n[-1])
	else:
		result += onesletters(n[-1])
	if x % 100 >= 20:
		result += twentiesletters(n[-2])
	if x >= 100:
		result += 10 # "hundred and"
		result += onesletters(n[-3])
		if x % 100 == 0:
			# remove "and"
			result -= 3
		if x % 1000 == 0:
			# remove "hundred"
			result -= 7
	if x >= 1000:
		# "thousand and"
		result += 11
		result += onesletters(n[-4])
		if x % 1000 == 0:
			result -= 3
		if x % 10000 == 0:
			result -= 8
print result