
"""1 :  Convert tuples to list."""


tup=(1,2,3,4,"hello")
lis=[]
for i in list(tup):
  lis.append(i)

print(lis)
print(list(tup))  

"""2 :  Write a program to calculate direction and magnitude of the vector described by the following points.
A = (20,30)
B = (30,40)"""


from math import sqrt,atan,degrees
x1,x2 = 20,30
y1,y2 = 30,40

mag=sqrt((pow(x2-x1,2)+pow(y2-y1,2)))

direct=atan((y2-y1)/(x2-x1))

print("The magnitude of the given coordinates is {}\nThe direction of the given coordinates is {}".format(round(mag,4),round(degrees(direct),4)))




"""3 :  Write a program to demonstrate data types that can be elements of a tuple"""

tup=(1,'a',"hello",[1,23],1.344,{"key":"value"})
for i in range(0,6):
  print(type(tup[i]))    