import random
import array


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



def quicksort(arr):
    if len (arr)<=1:
        return arr
    
    pivotFront=arr[0]
    pivotLast=arr[-1]
    pivotRandom=arr[random.randint(0,len(arr)-1)]
    pivotMedian = arr[len(arr)//2]

    i=arr.index(pivotFront)
    j=len(arr)-1
    i+=1

    while i<j:
        if arr[i]>pivotFront:
            swap(arr,i,j)
            j-=1
        else:
            i+=1
    if arr[i]>pivotFront:
        i-=1
    swap(arr,0,i)
    return quicksort(arr[:i])+[arr[i]]+quicksort(arr[i+1:])


#example usage 
arr=[10,1,2,14,6,8,20,11]
print(quicksort(arr))


def arrayQuicksort(arr):
    if len(arr)<=1:
        return arr
    pivotFront=arr[0]
    pivotLast=arr[-1]
    pivotRandom=arr[random.randint(0,len(arr)-1)]
    pivotMedian = arr[len(arr)//2]

    i=arr.index(pivotFront)
    j=len(arr)-1
    i+=1

    while i<j:
        if arr[i]>pivotFront:
            swap(arr,i,j)
            j-=1
        else:
            i+=1
    if arr[i]>pivotFront:
        i-=1
    swap(arr,0,i)
    return arrayQuicksort(arr[:i])+array.array('i',[arr[i]])+arrayQuicksort(arr[i+1:])


#usage
arr=array.array('i',[10,1,2,14,6,8,20,11])

print(arrayQuicksort(arr))

