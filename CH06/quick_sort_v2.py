def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    res = arr[1:]
    larr = [x for x in res if x <= pivot]
    rarr = [x for x in res if x > pivot]

    return quick_sort(larr) + [pivot] + quick_sort(rarr)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

print(quick_sort(arr))
