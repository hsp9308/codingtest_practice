# Binary search (Bisection)
# 
# For a sorted array, this function finds the target 
# with binary search method.
# There is a same method in the root-finding prolbem: bisection!

def binary_search(arr,target):
    l, r = 0, len(arr)-1

    if target == arr[l]:
        return l
    elif target == arr[r]:
        return r
    while l <= r:
        mid = (r+l) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1


def binary_search_recursive(arr,target,start,end):
    if start > end:
        return -1
    if target == arr[start]:
        return start
    elif target == arr[end]:
        return end

    mid = (start+end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr,target,start,mid-1)
    else:
        return binary_search_recursive(arr,target,mid+1,end)

arr = list(range(0,18,2))
print(binary_search(arr,4))
print(binary_search_recursive(arr,4,0,len(arr)-1))
