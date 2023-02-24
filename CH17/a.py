# 12시 방향부터 시계방향 순서대로 주어짐
# N : 0, S : 1
# 맞닿은 부분
# 2 = 3시 index
# 6 = 9시 index
from collections import deque

wheels = []
for _ in range(4):
    nums = input().rstrip()
    wheels.append(deque([int(x) for x in nums]))

K = int(input())
orders = []
for _ in range(K):
    a, b = map(int, input().split())
    orders.append((a, b))
# 회전 방향 = 1 : 시계
# 회전 방향 = -1 : 반시계


def rotate(arr, ind):
    if ind == 1:
        arr.appendleft(arr.pop())
    elif ind == -1:
        arr.append(arr.popleft())


for n, d in orders:
    rotate_ind = [0] * 4
    rotate_ind[n-1] = d
    for i in range(n-2, -1, -1):
        if rotate_ind[i+1] != 0 and wheels[i+1][6] != wheels[i][2]:
            rotate_ind[i] = rotate_ind[i+1]*(-1)
    for i in range(n, 4):
        if rotate_ind[i-1] != 0 and wheels[i-1][2] != wheels[i][6]:
            rotate_ind[i] = rotate_ind[i-1]*(-1)
    for i in range(4):
        rotate(wheels[i], rotate_ind[i])

answer = 0
for i in range(4):
    answer += wheels[i][0] * (2**i)
print(answer)
