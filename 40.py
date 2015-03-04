# Champernowne's constant

i = 1
nums = ''
while len(nums) < 1000000:
	nums += str(i)
	i += 1

print int(nums[0]) * int(nums[9]) * int(nums[99]) * int(nums[999]) * int(nums[9999]) * int(nums[99999]) * int(nums[999999])