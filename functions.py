'''Write a function that calculates the X^Y '''


# def power(x,y):
#     temp=1
#     for i in range(y):
#         temp*=x

#     print(temp)
    
# power(3,3)

'''Write a Python function to multiply all the numbers in a list.'''


# def multi(lis):
#     multi=1
#     for i in lis:
#         multi*=i

#     print(multi)

# lis=[10,20,30,100]

# multi(lis)

'''Write a Python function to calculate the factorial of a number (a non-negative integer).
 The function accepts the number as an argument.'''

# def fact(num):
#     facto=1
#     while num!=0:
#         facto*=num
#         print(num,end="*")
#         num-=1
#     print("=",facto)
# fact(5)

'''Write a Python function that accepts a string and calculates 
the number of uppercase letters and lowercase letters'''
from math import sqrt
import string


ch ='h'


# import string
# strings="Hello there Subash Tamang"

# def counting(strings):
#     uppercount=0
#     lowercount=0
#     for i in strings:
#         if i!=' ':
#             if i==i.upper():
#                 uppercount+=1
#             else:
#                 lowercount+=1

#     print(uppercount,lowercount)

# counting(strings)

'''Write a Python function that takes a list
 and returns a new list with unique elements of the first list'''
# lis=[1,1,2,3,'a','a','b']
# def unique(lis):
#     newlis=[]
#     for i in lis:
#         if i not in newlis:
#             newlis.append(i)

#     print(newlis)

# unique(lis)


'''Write a Python program to print the even numbers from a given list.
'''
# lis=[1,3,2,4,6,5,10,9]

# def even(lis):
#     newlis=[]
#     for i in lis:
#         if i%2==0:
#             newlis.append(i)
#     print(newlis)

# even(lis)


'''Write a Python function to check whether a string is a pangram or not.
 Note : Pangrams are words or sentences containing every letter of the alphabet at least once.'''
# import string
# sentance="The quick brown fox jumps over a lazy dog"
# nsentance="The quick brown fox jumps over a lazy "
# def is_pangrams(sentance):
#     flag=0
#     for i in string.ascii_lowercase:
#         if i not in sentance.lower():
#             flag+=1
#         else:
#             pass
#     if flag>0:
#         print("The sentence is not pangram") 

#     else:
#         print("The sentence is pangram")         
# is_pangrams(sentance)
# is_pangrams(nsentance)

'''Write a Python program that accepts a hyphen-separated sequence of words as input
 and prints the words in a hyphen-separated sequence after sorting them alphabetically
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''
# sample=[words for words in input().split('-')]
# sample.sort()

# print('-'.join(sample))

'''Write a Python program to reverse a string.
'''

# import string
# sti="Hello there"

# print(sti[::-1])

'''Write a Python program to access a function inside a function'''

# def student(Name,Roll,Grade):
#     def name():
#         print("NAME: ",Name)
#     def roll():
#         print("ROLL: ",Roll)
#     def grade():
#         print("Grade: ",Grade)
#     def intro():
#         name()
#         roll()
#         grade()
#     intro()

# student("Nihang",1,"A")

'''Write a program to double a given number and add two numbers using lambda()?'''
# num1=10
# num2=30

# sum=lambda x,y: x+y
# double=lambda x: num1*num1

# print(sum(num1,num2))
# print(double(num1))

'''Write a python module with two functions:
GCD
LCM
'''

# import smartmath

# print("Enter two numbers for GCD and LCM: ")
# num1=int(input())
# num2=int(input())
# Gcd=smartmath.GCD(num1,num2)
# Lcm=smartmath.LCM(num1,num2)
# print(Gcd)
# print(Lcm)

'''Write a python module with multiple sorting algorithms as its functions'''
# from smartmath import bubble_sort,insertion_sort,selection_sort
# lis1=[3,6,8,7,4,1,2,5]
# lis2=[10,40,50,70,20,30]
# lis3=[0,9,8,7,6,5,4,3,2]
# selection_sort(lis3)
# insertion_sort(lis2)
# bubble_sort(lis1)
# print(lis1)
# print(lis2)
# print(lis3)



'''Write three different functions to calculate the mean, variance and
 standard deviation of the following data.You need to call your mean function to
  within your variance and standard deviation functions.
S.N   Students    Marks
1      Richard      24
2       Lara        36
3       Prava       45
4       Peter       45
5       Judas       96
6       Jimmy       56
7       Jimi        89
8       Ronaldo     12
9       Messi       10
10      Pogba       100

'''

marks=[24,36,45,45,96,56,89,12,10,100]
def Mean(marks):
    sum=0
    for i in marks:
        sum+=i
    mean=sum/len(marks)
    return mean
    
    


def Variance(marks):
    res=[]
    for i in marks:
        res.append(round(pow((i-Mean(marks)),2),2))
    sum=0
    for i in res:
        sum+=i
    variance=sum/len(marks)

    return variance
    

def SD(marks):
    var=Variance(marks)

    sd=round(sqrt(var),2)

    return sd



print(Mean(marks))
print(Variance(marks))
print(SD(marks))