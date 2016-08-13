# Python Script to find is any given number is prime or not 
# First we find factor of that number Script of Factor 
def fac(n):
  res = []
  for i in range(1,n+1):
    if n%i == 0:
      res.append(i)
#Script to check prime or not
def prime(n):
    return(fac(n) == [1,n])
  
#Script print all prime number upto n
def prime_list(n):
  pri_list = []
  for i in range(1,n+1):
    if prime(i)
      pri_list.append(i)
  return(pri_list)

  
