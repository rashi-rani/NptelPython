# Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

# minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order

def frequency(l):
    minfreqlist = []
    maxfreqlist = []
    rl = []
    max = 0
    min = 0
    res = l[0]
    for i in l:
        freq = l.count(i)
        if freq > max:
            max = freq
            res = i
    maxfreqlist.append(res)
    for j in l:
        if j not in maxfreqlist:
            freq = l.count(j)
            if freq == max:
                maxfreqlist.append(j)
    min = max
    for i in l:
        freq = l.count(i)
        if freq < min:
            min = freq
            res = i
    minfreqlist.append(res)
    for j in l:
        if j not in minfreqlist:
            freq = l.count(j)
            if freq == min:
                minfreqlist.append(j)
    minfreqlist.sort()
    maxfreqlist.sort()
    rl = (minfreqlist, maxfreqlist)
    print(rl)
    return(rl)


frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7])
