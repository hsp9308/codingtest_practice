# 국영수 (백준 10825)
import sys
inp = sys.stdin.readline

N = int(inp())

arr = []

for _ in range(N):
    name, n1, n2, n3 = inp().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    arr.append((name, n1, n2, n3))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(arr[i][0])
