# Write a Python function onehop(l) that takes as input a list of pairs representing direct flights, as described above,
# and returns a list of all pairs (i,j), where i != j, such that i and j are connected by one hop.
# Note that it may already be the case that there is a direct flight from i to j.
# So long as there is an intermediate k with a flight from i to k and from k to j, the list returned by the function should include (i,j).
# The input list may be in any order. The pairs in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

# Here are some examples of how your function should work.


# >>> onehop([(2,3),(1,2)])
#[(1, 3)]

# >>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
#[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

# >>> onehop([(1,2),(3,4),(5,6)])
# []

def onehop(l):
    l1 = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] != l[j]:
                if l[i][1] == l[j][0]:
                    q = l[i][0]
                    w = l[j][1]
                    if q != w:
                        t = [q, w]
                        t = tuple(t)
                        if t not in l1:
                            l1.append(tuple(t))
    l1.sort()
    print(l1)
    return(l1)
onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])                        
