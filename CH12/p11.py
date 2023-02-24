# 뱀 (백준 3190)
N = int(input())
K = int(input())
dX = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

board = [[0]*N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

M = int(input())
orders = []
for _ in range(M):
    num, d = input().split()
    orders.append((int(num), d))
answer = 0
direction = 0
x, y = 0, 0
snake = [(x, y)]
snake_len = 1
num, r = orders.pop(0)
while True:
    if answer == num:
        if r == 'D':
            direction = (direction+1) % 4
        else:
            direction = (direction-1) % 4
        if orders:
            num, r = orders.pop(0)
    dx, dy = dX[direction]
    x, y = snake[0]
    nx, ny = x + dx, y + dy
    prev_pos = (x, y)
    answer += 1
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    elif (nx, ny) in snake[1:]:
        break
    snake[0] = (nx, ny)

    for i in range(1, snake_len):
        snake[i], prev_pos = prev_pos, snake[i]

    if board[nx][ny] == 1:
        snake_len += 1
        board[nx][ny] = 0
        snake.append(prev_pos)
    if (nx, ny) in snake[1:]:
        break


print(answer)
