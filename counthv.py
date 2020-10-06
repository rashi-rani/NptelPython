# In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
#Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.

def counthv(l):
    l1=[]
    (hc,vc)=(0,0)
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            hc=hc+1
            i=i+1
        elif l[i]<l[i-1] and l[i]<l[i+1]:
            vc=vc+1
            i=i+1
        else:
            i=i+1 
    l1.append(hc)
    l1.append(vc)
    print(l1)
    return(l1)  

l=[]
print("Enter the length of list: \n")
n=int(input())
print("Enter list items: \n")
for i in range(0,n):
    item=int(input())
    l.append(item)
    i=i+1
print("Your list is : l=",l)
    
counthv(l)             
