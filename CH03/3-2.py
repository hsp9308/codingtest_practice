import sys

inp = sys.stdin.readline

N, M, K = map(int, inp().split())

arr = list(map(int, inp().split()))

arr.sort()

first = arr[N-1]
second = arr[N-2]

cnt = (M // (K+1)) * K
cnt += M % (K+1)

answer = cnt*first
answer += (M-cnt)*second

print(answer)
