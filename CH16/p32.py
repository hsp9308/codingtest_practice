# 정수 삼각형 (백준 1932)
# 아래에서부터 위로 최적의 케이스를 골라가며 올라갔을 때,
# 꼭대기의 값이 최대경로의 값.
import sys
inp = sys.stdin.readline
N = int(inp())

board = []

for i in range(N):
    row = list(map(int, inp().split()))
    board.append(row+[0]*(N-1-i))

for i in range(N-2, -1, -1):
    for j in range(i+1):
        board[i][j] += max(board[i+1][j], board[i+1][j+1])

print(board[0][0])
