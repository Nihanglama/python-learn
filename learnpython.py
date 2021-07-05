from math import perm,comb,radians,sqrt,lcm
from random import randint


# Write a Python code to calculate Permutation (5,3)
n=5
r=3

print("The permutation of (5,3) is {}".format(perm(n,r)))
# Write a Python code to calculate Combination (15,3)
n=15
r=3

print("The combination of (15,3) is {}".format(comb(n,r)))

# Write a Python code that takes the degree as input from the user and convert it into radian.

degr= int(input("Enter the degree: "))

radn=radians(degr)

print(radn)

# Write a Python code that inputs input from the user and calculate its square root.

num=int(input("Enter the number : "))

sqroot= sqrt(num)
print("The square root of {} is {}".format(num,sqroot))


# Write a Python code to calculate LCM of (25,55)
print("The LCM of(25,55) is",lcm(25,55))


# Ask enter to enter two numbers (say, a and b). Generate two 
# random numbers between those two numbers and find a combination of these two newly generated 

a= int(input("Enter the number :"))
b= int(input("Enter another number:"))

num1=randint(a,b)
num2=randint(a,b)
print("The combination of ({},{}) is{}".format(num1,num2,comb(num1,num2)))

# Divide 1000 by 3 and print the answer with only 5 numbers after decimal.
numeritor= 1000
denuminator=3
div=1000/3
print("The division of 1000 and 3 is",round(div,5))

# Write a program to convert 108 to binary.
num=108
binary1=bin(108)
print("The binary if 108 is ",binary1)
# Write a program to convert 1008 to hexadecimal.
numb=1008
print("The hex of 1008 is ",hex(numb))

