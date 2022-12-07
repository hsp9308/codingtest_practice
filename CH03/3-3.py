import sys

inp = sys.stdin.readline

N, M = map(int, inp().split())

max_val = 0

for i in range(N):
    arr = list(map(int, inp().split()))
    temp = min(arr)
    if max_val < temp:
        max_val = temp

print(max_val)
