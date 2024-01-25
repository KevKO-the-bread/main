
def Quicksort(arr,l,r):
    if l>=r:
        return arr
    
    pivot=arr[r]
    left=l
    
    for i in range(l,r):
        if arr[i]<pivot:
            temp=arr[left]
            arr[left]=arr[i]
            arr[i]=temp
            left+=1
            
    arr[r] =arr[left]       
    arr[left]=pivot
    
    Quicksort(arr,l,left-1)
    Quicksort(arr,left+1,r)
    
    return arr

liste=[24,5,7,9,4,1,23,4,7,4,2,57,5,5,5]

print(Quicksort(liste, 0, len(liste)-1))
