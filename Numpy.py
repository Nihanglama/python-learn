# import numpy as np

# A = [
#     [1, 2, 3],
#     [55, 66, 7]
#   ]

# B =[
#     [5,4,3],
#     [6,-8,7],
#     [1,-1,10]
# ]

# C =[
#      [1, 2, 3, 8],
#     [5, 6, 7, 5],
#     [6, 7, 12, 12],
#     [11, 12, 13, 20]
#   ]

# def printMatrix(X):
#   for i in range(len(X)):
#     for j in range(len(X[0])):
#       print(f"  {X[i][j]}",end="")
#     print("")

# matrics = [A,B,C]
# xName = ['A','B','C']
# i = 0 
# for x in matrics:
#   print(f"The matrix {xName[i]} is:")
#   printMatrix(x)
#   print("")
#   try:
#     x_inverse = np.linalg.inv(x)
#     print(f"The inverse of matrix {xName[i]} is")
#     printMatrix(x_inverse)

#     print("")

#   except np.linalg.LinAlgError as laError:
#     print(f"[Error]: {laError}")
#   i+=1
  




'''Write a NumPy program to compute the eigenvalues and eigenvectors of a given square array.


B=[[1,2,3],
  [55,66,77],
  [6,7,12]
  ]
'''

# import numpy as np

# B=[[1,2,3],
#   [55,66,77],
#   [6,7,12]

#   ]
# print("Original matrix:")
# print("a\n", B)
# values, vectors = np.linalg.eig(B) 
# print( "Eigenvalues is: ",values)
# print( "Eigenvectors Is: ",vectors)











'''Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.'''

# import numpy as np

# arra1=np.zeros(10)
# arra2=np.ones(10)

# arra3=np.ones(10) *5

# print(arra1,arra2,arra3)



'''Write a NumPy program to generate five random numbers from the normal distribution.'''

# from numpy import random

# nums= random.normal(size=(1,5))
# print(nums)


'''Write a NumPy program to generate six random integers between 10 and 30.'''

# from numpy import random

# nums=random.randint(10,30,size=5)
# print(nums)

'''Write a NumPy program to create a 3x3x3 array with random values.'''

# from numpy import random


# arr=random.normal(size=(3,3,3))
# print(arr)


'''Write a NumPy program to create a 5x5 array with random values and find the minimum and maximum values.'''

# from numpy import random

# arr= random.normal(size=(5,5))
# print(arr)

'''Write a NumPy program to normalize a 3x3 random matrix.'''

# import numpy as np


# arr=np.random.random((3,3))
# print("The original matrix is \n:",arr)

# arrmax,arrmin=arr.max(),arr.min()
# arr=(arr-arrmax)/(arrmax-arrmin)


# print("The normalized matrix is :\n",arr)

'''Write a NumPy program to create a random vector of size 10 and sort it.'''
# import numpy as np


# vector=np.random.random(size=10)
# print(vector)
# vector1=np.sort(vector)
# print(vector1)

'''Write a NumPy program to check if two random arrays are equal or not.'''
# import numpy as np

# arr1=np.random.randint(1,3,4)
# arr2=np.random.randint(1,3,4)

# print("The First array is \n",arr1)
# print("The second array is \n",arr2)

# check_arr=np.allclose(arr1,arr2)
# if check_arr==True:
#   print("The two random array are equal")

# else:
#   print("The two array are not equal")



'''Write a NumPy program to create a random vector of size 15 and replace the maximum value by -1.'''
# import numpy as np

# vec=np.random.random(size=15)

# print("The vactor is \n",vec)
# print("\n The max value in vector is ",vec.max())

# vec[vec.argmax()]=-1

# print("The vector after replacing max value by -1 is :\n",vec)



'''Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on a flattened array.

A=[[1,2],
  [11,12]
  ]
'''
import numpy as np

A=np.array([[10,40],[20,30]])
print("The original array :\n",A)

print("The array after sorting alongfirst axis is:\n",np.sort(A,axis=0))
print("The array after sorting alonglast axis is:\n",np.sort(A))
print("The array after sorting along flattened array is:\n",np.sort(A,axis=None))
