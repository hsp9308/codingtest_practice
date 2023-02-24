# 퇴사 (백준 14501)

import sys
inp = sys.stdin.readline

N = int(inp())

schedule = []
for i in range(N):
    schedule.append(tuple(map(int, inp().split())))

S = [0] * (N+1)

max_income = 0

for i in range(N-1, -1, -1):
    t, s = schedule[i]
    time = t + i
    if time <= N:
        S[i] = max(S[time]+s, max_income)
        max_income = S[i]
    else:
        S[i] = max_income
print(max_income)
