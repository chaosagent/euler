# Coin sums

count = 0
for one in xrange(201):
	for two in xrange(101):
		if one + two * 2 > 200:
			break
		for five in xrange(41):
			if one + two * 2 + five * 5 > 200:
				break
			for ten in xrange(21):
				if one + two * 2  + five * 5 + ten * 10 > 200:
					break
				for twenty in xrange(11):
					if one + two * 2  + five * 5 + ten * 10 + twenty * 20 > 200:
						break
					for fifty in xrange(5):
						if one + two * 2  + five * 5 + ten * 10 + twenty * 20 + fifty * 50 > 200:
							break
						for hundred in xrange(3):
							if one + two * 2  + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred * 100 > 200:
								break
							for twohundred in xrange(2):
								if one * 1 + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred * 100 + twohundred * 200 == 200:
									count += 1
print count