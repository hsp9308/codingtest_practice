def qsort(arr):
    return quick_sort(arr,0,len(arr)-1)
def quick_sort(arr,start,end):
    if start >= end:    # len(arr) = 1 case
        return arr

    # pivot : Hoare Partition -> always first elements!
    pivot = start
    l, r = start + 1, end
    while l <= r:
        while l <= end and arr[l] <= arr[pivot]:
            l += 1
        while r > start and arr[r] >= arr[pivot]:
            r -= 1
        if l > r:
            arr[r], arr[pivot] = arr[pivot], arr[r]
        else:
            arr[l], arr[r] = arr[r], arr[l]
    quick_sort(arr,start,r-1)
    quick_sort(arr,r+1,end)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
qsort(arr)
print(arr)
