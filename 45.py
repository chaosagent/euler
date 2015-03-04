# Triangular, pentagonal, and hexagonal

n = 40756

triangles = set([])
pentagons = set([])
hexagons = set([])
for i in xrange(1,100001):
	triangles.add((i*(i+1))/2)
	pentagons.add((i*(3*i-1))/2)
	hexagons.add(i*(2*i-1))

print list(triangles & pentagons & hexagons)[-1]