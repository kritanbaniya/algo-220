
#insersion sort

def insersionsort(liist):
    lst = liist[:]
    for i in range(1,len(lst)):
        j = i
        while lst[j] < lst[j-1] and j > 0:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j = j-1
    return lst


def bubblesort(liist):
    lst = liist[:]
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def mergesort(liist):
    if len(liist) > 1:
        lsta = liist[:len(liist)//2]
        lstb = liist[len(liist)//2:]
        
        mergesort(lsta)
        mergesort(lstb)
        
        i = j = k = 0
        
        while i < len(lsta) and j < len(lstb):
            if lsta[i] < lstb[j]:
                liist[k] = lsta[i]
                i += 1
            else:
                liist[k] = lstb[j]
                j += 1
            k += 1            
        while i < len(lsta):
            liist[k] = lsta[i]
            i += 1
            k += 1
        
        while j < len(lstb):
            liist[k] = lstb[j]
            j += 1
            k += 1       
    

        
        
    return liist






liist = [12, 45, 23, 89, 67, 34, 90, 15, 8, 56]


#print (insersionsort(liist))
#print(bubblesort(liist))

print (mergesort(liist))


#print (liist)