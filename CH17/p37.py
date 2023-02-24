# 플로이드 (백준 11404)
import sys
inp = sys.stdin.readline
n = int(inp())
m = int(inp())
INF = 1e+9
adj = [[INF]*n for _ in range(n)]

for i in range(n):
    adj[i][i] = 0

for i in range(m):
    a, b, c = map(int, inp().split())
    adj[a-1][b-1] = min(adj[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

for i in range(n):
    for j in range(n):
        val = adj[i][j]
        if val != INF:
            print(val, end=' ')
        else:
            print(0, end=' ')
    print()
