# 정확한 순위
import sys
import copy
inp = sys.stdin.readline
N, M = map(int, inp().split())
INF = 987654321
adj = [[INF] * N for _ in range(N)]

for i in range(N):
    adj[i][i] = 0

for i in range(M):
    a, b = map(int, inp().split())
    adj[a-1][b-1] = 1
for k in range(N):
    for a in range(N):
        for b in range(N):
            adj[a][b] = min(adj[a][b], adj[a][k]+adj[k][b])
answer = 0
for i in range(N):
    count = 0
    for j in range(N):
        if adj[i][j] != INF or adj[j][i] != INF:
            count += 1
    if count == N:
        answer += 1
print(answer)
