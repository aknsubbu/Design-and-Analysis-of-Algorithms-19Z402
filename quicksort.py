import random
import array

def swap(a:int,b:int):
    return b,a

def quicksort(array:list[int], low:int, high:int) -> list[int]:
    if low == high:
        return array[low]
    
    pivot : int = low
    left : int = low + 1
    right : int = high

    while left < right:
        while array[pivot] > array[left]:
            left += 1

        while array[pivot] < array[right]:
            right -= 1

        if not left<right:
            break
        print('Swapping:',array[left],array[right])
        array[left], array[right] = swap(array[left], array[right])
    
    print('Swapping:',array[pivot],array[right])
    array[pivot], array[right] = swap(array[pivot], array[right])

    i = j = []

    if low <= right-1:
        i = quicksort(array, low, right-1)

    if right+1 <= high:
        j = quicksort(array, right+1, high)

    return i + [array[right]] + j

array = [3, 5, 1, 2, 4, 6, 7, 8, 9, 0]
print('The original list: ',array)
print('\n The sorted list:')
print(quicksort(array,0,len(array)-1))
