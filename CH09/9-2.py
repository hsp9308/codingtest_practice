import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())
INF = 987654321

distances = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    distances[i][i] = 0

for i in range(M):
    a, b = map(int, inp().split())
    distances[a][b] = 1
    distances[b][a] = 1

X, K = map(int, inp().split())

# 1에서 출발 K 방문 후 X 방문하는 최단 시간 계산
# -> Floyd-Warshall


def Floyd_Warshall(distances):
    N = len(distances)-1
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                distances[j][k] = min(distances[j][k],
                                      distances[j][i] + distances[i][k])


Floyd_Warshall(distances)

answer = distances[1][K] + distances[K][X]

if answer < INF:
    print(answer)
else:
    print(-1)
