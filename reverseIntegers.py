def intreverse(n):
  x = str(n)
  if len(x) == 1:
    return(n)
    
  else:
    endmsg = ""
    for i in range(0,len(x)):
      endmsg = x[i] + endmsg
    return(endmsg)  
