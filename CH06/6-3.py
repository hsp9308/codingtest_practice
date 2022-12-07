import sys
inp = sys.stdin.readline

N = int(inp())

arr = []

for _ in range(N):
    name, score = inp().split()
    arr.append((name, int(score)))

arr.sort(key=lambda x: x[1])

for e in arr:
    print(e[0], end=' ')
print()
