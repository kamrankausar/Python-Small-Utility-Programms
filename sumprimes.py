def sumprimes(l):
         sum = 0 
         for i in l:
             if i > 1:
                 prime = True
                 for j in range(2,i):
                     if (i%j == 0):
                        prime = False
                 if prime:
                    sum = sum + i
                                   
         return(sum)

