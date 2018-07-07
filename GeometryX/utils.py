import math

def area_of_triangle_heron_formula(a,b,c):
  ''' Calcultaing area of triangle using heron's formula.
  Formula: SQRT( s * (s-a) * (s-b) * (s-c) )
  where s is semi-perimeter of triangle sides(a,b,c)
  
  Arguments:
    a - side1 : Int/Float
    b - side2: Int/Float
    c - side3: Int/Float
  '''
  s = (a+b+c)/2
  return math.sqrt(s*(s-a)*(s-b)*(s-c))
