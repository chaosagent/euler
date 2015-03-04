# Reciprocal cycles
import decimal
import re
def repetitions(s):
   r = re.compile(r"(.+?)\1+")
   for match in r.finditer(s):
       yield (match.group(1), len(match.group(0))/len(match.group(1)))
def reps(s):
	return list(repetitions(s))
from decimal import Decimal as dec
decimal.getcontext().prec = 2000
largest = 0
largestn = 0
largestnt = 0
for n in xrange(1,1000):
	rec = dec(1) / dec(n)
	rec = str(rec)[2:]
#	print reps(recs)
	segs = sorted(reps(rec), cmp=lambda x,y: cmp(len(y[0]),len(x[0])))
	if len(segs) == 0:
		continue
	length = len(segs[0][0])
	if length > largest:
		largest = length
		largestn = n
		largestnt = segs[0][1]
print largestn