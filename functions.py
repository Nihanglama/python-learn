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
sample=[words for words in input().split('-')]
sample.sort()

print('-'.join(sample))
    