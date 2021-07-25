'''Count the total number of words in ‘oliver.txt’.'''

# file= open('oliver.txt')
# i=0
# for lines in file:
#     word=lines.split()
#     i+=len(word)
    
# print("There are {} in the oliver.txt".format(i))
    

'''Make a dictionary of all the unique words and their frequency  in ‘oldman.txt’.'''
# dict={}
# lis=[]
# file =open('oldman.txt','r')
# for lines in file.readlines():
#     word = lines.replace('"', '').replace("?", "").replace(".", "").replace(",", '').replace("[",'').replace("]",'').replace("_",'')
#     word=word.split()
#     for i in word:
#         lis.append(i)

# for i in lis:
#     if i not in dict:
#         a=lis.count(i)
#         dict.update({i:a})

# print(dict)
 


'''Make a dir named ‘Books’. Make 26 directories inside ‘Books’ from A-Z. Put the following files in the following directories.

Files            Folders
Oldman.txt          O
oliver.txt          O
Alice.txt           A
Siddhartha.txt      S
hitler.txt          H
history.txt         H

'''

import os
from posix import listdir
import shutil
import string

# main='Books/'
# folders=[x for x in string.ascii_uppercase]
# for folder in folders:
#     os.makedirs(main+folder)

# files=['oldman.txt','oliver.txt','Alice.txt','Siddhartha.txt','hitler.txt','history.txt']
# cd=os.getcwd()
# for sub_dir in os.listdir('Books'):
#     for i in files:
#         if sub_dir.lower()==i[0].lower():
#             shutil.copy(f'{cd}/{i}',main+sub_dir)
            


'''Write a program that asks the user to enter the name of a book.
 If the book is in your library print its first line. 
 If it is not in your library, handle the exception appropriately.'''

# book_name=input("Enter the book name: ")
# paths='library/'
# try:
#     with open(paths+book_name,'r') as f:
#         print(f.readline())

# except FileNotFoundError as e:
#     # print(e)
#     print("Book doesn't Exists")


'Calculate the sum of all numbers that appear after decimal in ‘pi_million_digits.txt’.'

      
# file =open('pi_million_digits.txt','r')
# from time import sleep
# num=[]
# for i in file.read():
#     if i.isnumeric():
#         num.append(int(i))

# add=sum(num[1::])
# print(add)


'''Print all the numbers present in ‘hitler.txt’.'''

# file =open("hitler.txt",'r')

# for i in file.readlines():
#     num=i.split()
#     for j in num:
#         if j.isdigit():
#             print(j)

'''Extract all the years (e.g 1994) from the file ‘history.txt’ 
and save it in another file named ‘year.txt’.'''

file =open("history.txt",'r')
file1=open('years.txt','w')
for i in file.readlines():
    num=i.replace('(','').replace(')','').replace('-','').replace('"', '').replace("?", "").replace(".", "").replace(",", '').replace("[",'').replace("]",'').replace("_",'')
    num=num.split()
    for j in num:
        if j.isdigit() and len(j)==4:
            file1.write("{}\n".format(j))








 