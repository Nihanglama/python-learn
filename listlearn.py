"""1. Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’."""


# lis=['biki','Binod','sabin','sachin','binita']


# for i in range(0,5):
#     a=lis[i]
#     if a[0]=='b'or a[0]=='B':
#         print(a)

"""buildin function"""


# lis=['Biki','Binod','sabin','sachin','Binita']

# for i in lis:
#     a=i.startswith('B')
#     if a ==True:
#         print(i)


"""2. Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’."""

# lis=['Biki','Binod','sabina','sachin','Binita']

# for i in lis:
#     if i[-1]=='a':
#         print(i)



"""BUild in function """
# lis=['Biki','Binod','sabin','sachin','Binita']

# for i in lis:
#     a=i.endswith('a')
#     if a== True:
#         print(i)



"""3.   Print all the unique elements in the following list 
fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']"""


# fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']

# unififa=[]
# for i in fifa:
#     a=fifa.count(i)
#     if a>1:
#         pass
#     else:
#         unififa.append(i)

# print(unififa)


"""4.   Change the first alphabet of all elements of the following list to capital.
Bob = [‘hurricane’,’tambourine’,’blowing’,’numb’]
"""
# Bob =['hurricane','tambourine','blowing','numb']
# Bob1=[]
# for i in Bob:
#     a=i.replace(i[0],i[0].upper())
    
#     Bob1.append(a)

# print(Bob1)


"""5. A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]
Find  AUB and AnB """


# A = ['a','b','c','d']
# B = ['1','a','2','b']

# AuB=[]
# AnB=[]
# for i in A:
#     if i not in AuB:
#         AuB.append(i)
# for i in B:
#     if i not in AuB:
#         AuB.append(i)

# for i in A:
#     if i in B:
#         AnB.append(i)
# print(AuB)
# print(AnB)

"""Build in"""
# A = ['a','b','c','d']
# B = ['1','a','2','b']

# print(set(A)|set(B))
# print(set(A)&set(B))


"""6.   Calculate the mean and standard deviation of the following list:
Numbers = [1,2,3,5,88,99,55,33,41,52]
"""
# from math import sqrt
# Numbers = [1,2,3,5,88,99,55,33,41,52]

# Ex=sum(Numbers)
# N=len(Numbers)
# Ex2=0
# for i in Numbers:
#     Ex2+=i*i
# mean=Ex/N
# print(mean)

# SD=sqrt(Ex2/N-pow(mean,2))

# print(SD)


"""Build in"""
# from statistics import mean,stdev
# Numbers = [1,2,3,5,88,99,55,33,41,52]
# print(mean(Numbers))
# print(stdev(Numbers))


from math import cos,sin

def deveq(x):
  eq=-(sin(x))-0.5
  return eq


def eqcal(x):
  eq = cos(x)-0.5*x+2
  return eq

def finalShow(x):
  i=1
  xo=x
  for i in range(1,11):
    Xn= xo-(eqcal(xo)/deveq(xo))
    print("Iteration {}\n X{}={}\tf(X{})={}\tf'(X{})={}".format(i ,i, round(Xn,4),i-1,round(eqcal(xo)),i-1,round(deveq(xo))))
    xo=Xn
    i+=1


finalShow(x=-3)
