


def nprime(n):
          (count,i,plist) = (0,1,[])
          while(count < n):
              if prime(i):
                  (count,plist) = (count+1,plist+[i])
              i = i + 1
          return(plist)
