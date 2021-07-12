"""Write a python program to find the largest of three numbers ."""

# a=50
# b=6
# c=10

# if a>b and a>c:
#     print("{} is greatest".format(a))
# elif b>c:
#     print("{} is greatest".format(b))
# else:
#     print("{} is greatest".format(c))


"""Write a python program to check whether a character is uppercase or lowercase alphabet."""

# cha=str(input("Give a character:  "))

# if cha.isupper()==True:
#     print("The characte is upper")
# elif cha.islower()==True:
#     print("The character is lower")
# else:
#     print("Undefined")


"""WAP to find whether given input is number or character."""
# inp=input("Give the input:")

# if inp.isalpha()==True:
#     print("The given input is character ")
# elif inp.isalnum()==True:
#     print("The given input is number")

"""Write a program to check whether the input alphabet is vowel or not using if-else."""

# cha= str(input("Enter the character "))
# def isvowel(ch):
#    vowel=['a','e','i','o','u','A','E','I','O','U']
#    if ch in vowel:
#        return True
#    else:
#         return False

# if isvowel(cha)==True:
#     print("Is vowel")


"""Write a program to check whether the entered year is leap year or not."""

# year=int(input("Enter thq year: "))

# if (year % 4) == 0:  
#    if (year % 100) == 0:  
#        if (year % 400) == 0:  
#            print("{} is a leap year".format(year))  
#        else:  
#            print("{} is not a leap year".format(year))  
#    else:  
#        print("{} is a leap year".format(year))  
# else:  
#    print("{} is not a leap year".format(year))



"""Write a program to check if the number is Armstrong or not."""

# num= int(input("Enter the number: "))

# relnum=num
# sum=0
# while num>0:
#     r=num%10
#     sum+=(r*r*r)
#     num=int(num/10)

# if relnum==sum:
#     print("The number is armstrong")
# else:
#     print("The number is not armstrong")



"""Write a program to compute the grade from marks. 

Marks                   Grade
Marks<=50                  F
60>=marks>50               E
70>= marks > 60            D
80>= marks > 70            C
90 > = marks > 80          B
100>= marks >90            A
"""

marks= int(input("Enter the marks: "))

if marks<=50:
    print("Your grade is F ")
elif marks>50 and marks<=60:
    print("Your grade is E ")
elif marks>60 and marks<=70:
    print("Your grade is D ")
elif marks>70 and marks <=80:
    print("Your grade is C ")
elif marks>80 and marks <=90:
    print("Your grade is B ")
elif marks>90 and marks <=100:
    print("Your grade is A ")
else:
    print("Invalid marks ")
