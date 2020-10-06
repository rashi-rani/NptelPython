# Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases 

def contracting(l):
    dl=[]
    (i,j)=(0,0)
    for i in range(0,len(l)-1):
        diff=abs(l[i]-l[i+1])
        dl.append(diff)
        i=i+1
    for j in range(0,len(dl)-1):
        if dl[j]>dl[j+1]:
            j=j+1
        else:
            print("False")
            return(False)
    print(dl)        
    return(True)

l=[]
print("Enter the length of list: \n")
n=int(input())
print("Enter list items: \n")
for i in range(0,n):
    item=int(input())
    l.append(item)
    i=i+1
print("Your list is : l=",l)
    
contracting(l)
                 