import math
a = 2.5
b = 1.7
c = 0.3
d = 5.4

n1 = ((a**2 + 3*b) / c) + d
n2 = (math.log10(a) + (math.e) **( -b/c) - (d**2 / math.pi))
n3 = ((a**2)**1/3)*(b**(1/3)) + (c*d) / (a+b+c+d)
n4 = (a + b) * (c + d) / (a * b * c * d)
n5 = (((a**2) + (b**2)) /(c*d)) - ((c**2) + (d**2))/(a*b)
n6 = (a + b + c + d)**2
n7 = ((a**2)+(b**2)+(c**2)+(d**2))
n8 = (a * b * c * d ) ** (1/3)

print(round(n1,4))
print(round(n2,4))
print(round(n3,4))
print(round(n4,4))
print(round(n5,4))
print(round(n6,4))
print(round(n7,4))
print(round(n8,4))
