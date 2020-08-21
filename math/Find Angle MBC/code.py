# import math
# import numpy
# ab=int(input())
# bc=int(input())
# c=ab**2+bc**2
# print(c)
# c=math.sqrt(c)
# print(c)
# c=c/2
# print(c)

# c=round(c,3)
# print(c)

# # print(c)
# print(c/bc)
# print(math.asin(1))
# print(numpy.arcsin(1))

import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle 
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')