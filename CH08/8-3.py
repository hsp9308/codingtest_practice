import sys
inp = sys.stdin.readline

N = int(inp())

A = list(map(int, inp().split()))

d = [0] * 100
d[0] = A[0]
d[1] = max(A[0], A[1])
max_val = 0

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+A[i])

print(d[N-1])
