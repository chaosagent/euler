# Distinct powers

nums = []
for a in xrange(2,101):
	for b in xrange(2,101):
		x = a**b
		if x not in nums:
			nums.append(x)
print len(nums)