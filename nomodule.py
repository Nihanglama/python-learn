# Write a Python code to calculate Permutation (5,3)
n=5
r=3

def per(n,r):
  nr=n-r
  nrfac=1
  nfac=1
  while n!=0:
    nfac*=n
    n-=1
  while nr!=0:
    nrfac*=nr
    nr-=1
  
  print("The permutaion of (5,3) is {}".format(nfac/nrfac))
per(n,r)

# Write a Python code to calculate Combination (15,3)
n=15
r=3
nr=(n-r)

def comb(n,r,nr):
  nfac=1
  rfac=1
  nrfac=1
  while n!=0:
    nfac*=n
    n-=1
  while r!=0:
    rfac*=r
    r-=1
  while nr!=0:
    nrfac*=nr
    nr-=1
  print("The combination of (15,3) is {}".format(nfac/(rfac*nrfac)))

comb(n,r,nr)


# Write a Python code that takes the degree as input from the user and convert it into radian.

degree=int(input("Enter the degree to convert: "))
pi=3.141
convert=lambda degree,pi: degree*(pi/180)
print(convert(degree,pi))

# Write a Python code that inputs input from the user and calculate its square root.

num= int(input("Enter the number to find square root: "))
sqroot=lambda num:pow(num,0.5)
print(sqroot(num))