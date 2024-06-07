#min max algo using divide and conquer

def minmax(arr,low,high):
    if low==high:
        return arr[low],arr[low]
    elif low==high-1:
        if arr[low]>arr[high]:
            return arr[high],arr[low]
        else:
            return arr[low],arr[high]
    else:
        mid=(low+high)//2
        min1,max1=minmax(arr,low,mid)
        min2,max2=minmax(arr,mid+1,high)
        return min(min1,min2),max(max1,max2)
arr=[1,2,3,4,5,6,7,8,9]
low=0
high=len(arr)-1
min1,max1=minmax(arr,low,high)
print("Minimum element is",min1)

print("Maximum element is",max1)
