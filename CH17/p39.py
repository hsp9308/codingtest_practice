# 화성 탐사
import sys
import heapq
inp = sys.stdin.readline

T = int(inp())

dX = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra(graph, visited, x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    N = len(graph)
    while q:
        c, x, y = heapq.heappop(q)
        if visited[x][y] != 0:
            continue
        visited[x][y] = c + graph[x][y]
        for dx, dy in dX:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            elif visited[nx][ny] == 0:
                heapq.heappush(q, (visited[x][y], nx, ny))


answer = []
for _ in range(T):
    N = int(inp())
    graph = []
    for i in range(N):
        row = list(map(int, inp().split()))
        graph.append(row)
    visited = [[0]*N for _ in range(N)]
    dijkstra(graph, visited, 0, 0)
    answer.append(visited[N-1][N-1])

for num in answer:
    print(num)
