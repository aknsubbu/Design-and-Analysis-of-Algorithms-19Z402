def mergeSort(array:list) -> list:

    def merge(left:list, right:list) -> list:
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        # the .extend function will add the remaining elements of the non-empty list to the result
        result.extend(left)
        result.extend(right)
        return result
    
    if len(array) <= 1:
        return array
    
    midIndex = len(array) // 2
    left = mergeSort(array[:midIndex])
    right = mergeSort(array[midIndex:])
    return merge(left, right)


array = [3, 5, 1, 2, 4, 6, 7, 8, 9, 0]
print('The original list: ',array)
print('\n The sorted list:')
print(mergeSort(array))
