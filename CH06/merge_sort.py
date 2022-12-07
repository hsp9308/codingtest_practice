def merge_sort(arr):
    if len(arr) < 2:
        return arr
    m = len(arr)//2
    larr = merge_sort(arr[:m])
    rarr = merge_sort(arr[m:])

    res = []
    l = 0
    r = 0
    while l < len(larr) and r < len(rarr):
        if larr[l] < rarr[r]:
            res.append(larr[l])
            l += 1
        else:
            res.append(rarr[r])
            r += 1

    res += larr[l:]
    res += rarr[r:]
    return res


if __name__ == '__main__':
    A = [5,3,1,35,8,9,1,1,593,3,8,1,20]
    A = merge_sort(A)
    print(A)
