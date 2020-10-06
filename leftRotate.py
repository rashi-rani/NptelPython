#  A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

#   1  2  3
#   4  5  6
#   7  8  9 
# would be represented as [[1,2,3], [4,5,6], [7,8,9]].

# Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get

#   3  6  9
#   2  5  8    
#   1  4  7 

def leftrotate(m):
    k=len(m)
    l=[]
    n=k
    for x in range(0,k):
        a=[]
        for y in range(0,k):
            a.append(0)
        l.append(a)
        
    for i in range (0,k):
        for j in range(0,k):
            l[i][j]=m[j][n-1]
            j=j+1
        n=n-1
        j=0 
    print(l)    
    return(l)

m=[[1,2,3], [4,5,6], [7,8,9]]
leftrotate(m)
