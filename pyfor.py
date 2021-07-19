'''Multiply following matrices
A=[[1,2,3],
  [4,5,6],
  [7,8,9]]

b=[[111,22,33],
   [44,55,56],
   [47,86,19]]

Using for loops and print the result.
'''
# A = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
#   ]
# B = [
#   [111, 22, 33],
#   [44, 55, 56],
#   [47, 86, 19]  
#   ]
# matrix_mul = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(3):
#   for j in range(3):
#     for k in range(3):
#       matrix_mul[i][j] += A[i][k] * B[k][j]

# print("The result of the multiplication of given two matrix is \n: ".format(A,B))

# for i in range(len(matrix_mul)):
#   for j in range(len(matrix_mul[i])):
#     print(f"{matrix_mul[i][j]}",end=" ")
#   print("")


'''
Multiply following matrices


C=[[111,22,33,44],
   [44,55,56,1],
   [47,86,19,2],
   [1,2,22,3]]

D=[[11,22,3,4],
  [4,5,6,1],
  [7,6,19,2],
  [1,2,22,3]]

'''

# C=[[111,22,33,44],
#    [44,55,56,1],
#    [47,86,19,2],
#    [1,2,22,3]]

# D=[[11,22,3,4],
#   [4,5,6,1],
#   [7,6,19,2],
#   [1,2,22,3]]

# matrix_mul = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# for i in range(4):
#   for j in range(4):
#     for k in range(4):
#       matrix_mul[i][j] += C[i][k] * D[k][j]

# print("The result of the multiplication of given two matrix is \n: ".format(A,B))

# for i in range(len(matrix_mul)):
#   for j in range(len(matrix_mul[i])):
#     print(f"{matrix_mul[i][j]}",end=" ")
#   print("")




'''
F
FFF
FFFFF
FFFFFFF
FFFFFFFFF
FFFFFFFFFFF'''


# temp=3
# for i in range(0,6):
#     if i==0:
#         print("F")
#     else:
#         for j in range(0,temp):
#             print("F",end=" ")
#         temp+=2  
#         print(" ")   



# F        
# F         
# FF        
# FFF       
# FFFFF     
# FFFFFFFF  
# FFFFFFFFFFFFF
# FFFFFFFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF 
first= 1
second = 1

for i in range(1, 10):
  if (i == 1 or i == 2):
    print("F",end="")
  else:
    next = first + second
    for j in range(next):
      print("F", end="")
    first = second
    second = next
  print("")