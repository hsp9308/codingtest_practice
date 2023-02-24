# 경쟁적 전염 (백준 18405)
import sys
from collections import deque
inp = sys.stdin.readline
N, K = map(int, inp().split())

board = [[0]*(N+1) for _ in range(N+1)]
q = []
for i in range(N):
    row = list(map(int, inp().split()))
    for j in range(N):
        if row[j] != 0:
            q.append((row[j], i+1, j+1, 0))

S, X, Y = map(int, inp().split())
dX = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q.sort()
q = deque(q)

while q:
    now, x, y, t = q.popleft()
    if t > S:
        break
    if board[x][y] != 0:
        continue
    board[x][y] = now
    for dx, dy in dX:
        nx, ny = x + dx, y + dy
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        elif board[nx][ny] == 0:
            q.append((now, nx, ny, t+1))

print(board[X][Y])
