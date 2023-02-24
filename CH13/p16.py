# 연구소 (백준 14502)
# BFS로 처리해보자!

from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())

empty = []
virus = []
maps = []
answer = 0

for i in range(N):
    row = list(map(int, input().split()))
    maps.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))


def BFS(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        if graph[x][y] != 0:
            continue
        graph[x][y] = 2
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif graph[nx][ny] == 0:
                q.append((nx, ny))


for O in combinations(empty, 3):
    board = copy.deepcopy(maps)
    count = 0
    for x, y in O:
        board[x][y] = 1
    for x, y in virus:
        BFS(board, x, y)
    for row in board:
        count += row.count(0)
    answer = max(count, answer)

print(answer)
