# 금광
# 이전 열의 상중하 열을 확인하면서 계속 업데이트하면 됨.
import sys
inp = sys.stdin.readline
T = int(inp())
answer = []
for _ in range(T):
    n, m = map(int, inp().split())
    board = []
    arr = list(map(int, inp().split()))
    for i in range(n):
        board.append(arr[i*m:(i+1)*m])
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = board[i][0]

    for i in range(1, m):
        for j in range(n):
            n1 = n2 = n3 = 0
            n2 = dp[j][i-1]
            if j > 0:
                n1 = dp[j-1][i-1]
            if j < n-1:
                n3 = dp[j+1][i-1]
            dp[j][i] = board[j][i] + max(n1, n2, n3)
    res = 0
    for i in range(n):
        res = max(res, dp[i][m-1])
    answer.append(res)

for num in answer:
    print(num)
