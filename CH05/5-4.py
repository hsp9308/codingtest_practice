from collections import deque
import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, inp().rstrip())))

visited = [[0]*M for _ in range(N)]


def BFS(graph, x, y):
    depth = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = depth
    dX = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        depth = graph[x][y]
        for dx in dX:
            nx, ny = x + dx[0], y + dx[1]
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = depth+1
    return


BFS(graph, 0, 0)
print(graph[N-1][M-1])
