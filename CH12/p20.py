# 감시 피하기 (백준 18428)
from itertools import combinations
N = int(input())

board = []
teacher = []
empty = []

for i in range(N):
    row = input().split()
    board.append(row)
    for j in range(N):
        if row[j] == 'X':
            empty.append((i, j))
        elif row[j] == 'T':
            teacher.append((i, j))
dX = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def search():
    for xt, yt in teacher:
        for dx, dy in dX:
            x, y = xt, yt
            while True:
                x, y = x + dx, y + dy
                if x < 0 or x >= N or y < 0 or y >= N:
                    break
                elif board[x][y] == 'O':
                    break
                elif board[x][y] == 'S':
                    return False
    return True


answer = False
for E in combinations(empty, 3):
    for x, y in E:
        board[x][y] = 'O'
    if search():
        answer = True
        break
    for x, y in E:
        board[x][y] = 'X'

if answer:
    print("YES")
else:
    print("NO")
