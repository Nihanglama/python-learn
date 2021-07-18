# F
# FFF
# FFFFF
# FFFFFFF
# FFFFFFFFF
# FFFFFFFFFFF
# temp=3
# for i in range(0,6):
#     if i==0:
#         print("F")
#     else:
#         for j in range(0,temp):
#             print("F",end=" ")
#         temp+=2  
#         print(" ")   

# F         odd
# F         even
# FF        odd
# FFF       even
# FFFFF     odd
# FFFFFFFF  even
# FFFFFFFFFFFFF
# FFFFFFFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

# for i in range(0,9):
#     for j in range()
 

stri= "NihangLama"

def compare(stri):
    up=0
    lo=0
    for i in stri:
        if i== i.upper(): 
            up+=1
        else:        
            lo+=1

    print("There are {} upper and {} lower case words in {}".format(up,lo,stri)) 

compare(stri)

