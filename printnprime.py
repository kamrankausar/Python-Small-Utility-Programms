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
  
#Script print n prime numbers 
def nprime(n):
          (count,i,plist) = (0,1,[])
          while(count < n):
              if prime(i):
                  (count,plist) = (count+1,plist+[i])
              i = i + 1
          return(plist)
