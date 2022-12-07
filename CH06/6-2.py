import sys
inp = sys.stdin.readline

N = int(inp())

arr = []
for _ in range(N):
    arr.append(int(inp()))

#  mergesort


def sort_arr(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    larr = arr[:mid]
    rarr = arr[mid:]
    larr = sort_arr(larr)
    rarr = sort_arr(rarr)
    res = []
    l, r = 0, 0
    while l < len(larr) and r < len(rarr):
        if larr[l] <= rarr[r]:
            res.append(larr[l])
            l += 1
        else:
            res.append(rarr[r])
            r += 1
    res += larr[l:]
    res += rarr[r:]
    return res

# # Quick sort
# def sort_arr(arr):
#     if len(arr) < 2:
#         return arr

#     pivot = arr[0]
#     res = arr[1:]

#     larr = [x for x in res if x <= pivot]
#     rarr = [x for x in res if x > pivot]

#     return sort_arr(larr) + [pivot] + sort_arr(rarr)


arr = sort_arr(arr)[::-1]

for n in arr:
    print(n, end=' ')
print()
