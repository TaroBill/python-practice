import math
a,b,c = int(input()),int(input()),int(input())
x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
print("%.1f" %x1)
print("%.1f" %x2)