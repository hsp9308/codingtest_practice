# 병사 배치하기 (백준 18353)
N = int(input())

arr = list(map(int, input().split()))

arr.reverse()

d = [1]*N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j]+1)

print(N-max(d))
