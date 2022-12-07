import sys
inp = sys.stdin.readline

N = int(inp())

storage = sorted(list(map(int, inp().split())))

M = int(inp())

quest = list(map(int, inp().split()))


def binary_search(arr, target):
    l, r = 0, len(arr)-1
    if arr[l] == target:
        return l
    elif arr[r] == target:
        return r

    while l <= r:
        mid = (l+r) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            r = mid-1
        else:
            l = mid+1
    return -1


for n in quest:
    val = binary_search(storage, n)
    if val == -1:
        print("no", end=" ")
    else:
        print("yes", end=" ")
print()
