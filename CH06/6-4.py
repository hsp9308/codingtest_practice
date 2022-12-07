import sys
inp = sys.stdin.readline

N, K = map(int, inp().split())

arr1 = sorted(list(map(int, inp().split())))
arr2 = sorted(list(map(int, inp().split())), reverse=True)

# 최악의 경우, arr2의 모든 원소가 arr1보다 클 수 있음.
for i in range(K):
    if arr2[i] > arr1[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break
print(sum(arr1))
