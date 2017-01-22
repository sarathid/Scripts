# from socket import *

# print gethostbyname('google.com')
# print getfqdn('google.com')
# print getaddrinfo('google.com' ,80)
# print gethostbyaddr('216.58.196.110')

from math import acos, sqrt, radians, degrees
from decimal import *
getcontext().prec = 6

def vectorMag(v):
	return Decimal(sqrt(sum([(Decimal(x))**2 for x in v])))

def vector_add(v,w):
	return [(Decimal(x[0]))+(Decimal(x[1])) for x in zip(v,w)]

def vector_sub(v,w):
	return [(Decimal(x[0]))-(Decimal(x[1])) for x in zip(v,w)]

def dot_prod(v,w):
	return sum([(Decimal(x[0]))*(Decimal(x[1])) for x in zip(v,w)])

def unit_vector(v):
	m = vectorMag(v)
	print v
	try:
		return [Decimal(x)/Decimal(m) for x in v]
	except:
		print 'Error'

def mulVector(v, m):
	return [Decimal(x)*Decimal(m) for  x in v]

def angle(v,w, deg=False):
	try:
		# print vectorMag(v)
		# print vectorMag(w)
		# print dot_prod(v,w)
		r = acos(dot_prod(v,w)/(vectorMag(v)*vectorMag(w)))
		return r if deg is False else degrees((Decimal(r)))
	except:
		print 'Pass'

def cross_prod(v,w):
	x1 = Decimal(v[0])
	y1 = Decimal(v[1])
	z1 = Decimal(v[2])
	x2 = Decimal(w[0])
	y2 = Decimal(w[1])
	z2 = Decimal(w[2])
	result = []
	result.append(y1*z2 - y2*z1)
	result.append(-(x1*z2 - x2*z1))
	result.append(x1*y2 - x2*y1)
	return result
	
def area_of_parallogram(v,w):
	vxw = cross_prod(v,w)
	return vectorMag(vxw)

def area_of_triangle(v,w):
	return area_of_parallogram(v,w)/2

# print angle([-7.579,-7.88],[22.737, 23.64])
# print angle([3.183,-7.627],[-2.668, 5.319])
# print angle([-7.579,-7.88],[22.737, 23.64])
# print angle([-2.029,9.97,4.172],[-9.231,-6.639,-7.245])
# print angle([-2.328,-7.284,-1.214],[-1.821,1.072,-2.94])
# print angle([2.118,4.827],[0, 0])

# v = [3.039, 1.879]
# b = [0.825, 2.036]
# ub = unit_vector(b)
# print ub
# dpub = dot_prod(v, ub)

# if angle(v,b, True)>=90:
# 	dpub = -dpub

# print 'Mul ', mulVector(ub, dpub)

# v = [-9.88, -3.264, -8.159]
# b = [-2.155, -9.353, -9.473]
# ub = unit_vector(b)
# print 'Unit vector', ub
# dpub = dot_prod(v, ub)
# print 'Dot prod',dpub
# print 'Angle',angle(v,b, True)

# if angle(v,b, True)>=90:
# 	dpub = -dpub

# vp = mulVector(ub, dpub)
# vper = vector_sub(v, vp)
# print 'Vector parallel', vper


# v = [3.009, -6.172, 3.692, -2.51]
# b = [6.404, -9.144, 2.759, 8.718]
# ub = unit_vector(b)
# print ub
# dpub = dot_prod(v, ub)

# if angle(v,b, True)>=90:
# 	dpub = -dpub

# vp = mulVector(ub, dpub)
# vper = vector_sub(v, vp)
# print 'Vector Parallel',vp 
# print 'Vector perp', vper


v = [8.462, 7.893, -8.187]
w = [6.984, -5.975, 4.778]

print 'Cross-prod ',cross_prod(v,w)

v = [-8.987, -9.838, 5.031]
w = [-4.268, -1.861, -8.866]

print 'Area of parall', area_of_parallogram(v,w)

v = [1.5, 9.547, 3.691]
w = [-6.007, 0.124, 5.772]
print 'Area of Triangle', area_of_triangle(v,w)