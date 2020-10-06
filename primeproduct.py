def prime(n):
    if n>1:
        for i in range(2, n):
            if (n % i) == 0: 
                return(False)
                break                
        else:
            return(True)
    else:
        return(False)                 
   
def primeproduct(m):
    [i,j]=[0,0]
    for i in range(2,m+1):
        if (m%i)==0:
            if prime(i)==True :
               j=m//i
               if prime(j)==True:
                   print("primeproduct")
                   return(True)
                   break
                 
        else:
            i=i+1
    print("notprime")
    return(False)
m=int(input())
primeproduct(m)
            

             
                             
