def floyd_marshall(distance):
    N = len(distance) - 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                distance[j][k] = min(distance[j][k],distance[j][i]+distance[i][k])

import sys
inp = sys.stdin.readline
N, M = map(int,inp().split())
INF = 987654321
distance = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i] = 0
for i in range(M):
    a, b = map(int,inp().split())
    distance[a][b] = 1
    distance[b][a] = 1

floyd_marshall(distance)

X, K = map(int,inp().split())
answer = distance[1][K] + distance[K][X]
if answer < INF:
    print(answer)
else:
    print(-1)
