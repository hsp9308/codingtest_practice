# 공유기 설치 (2110)
# 최소 거리와 최대 거리를 가지고 이진탐색
# 만들 수 있는 공유기의 개수를 계속 카운트하면서 범위를 좁혀감.
import sys
inp = sys.stdin.readline

N, C = map(int, inp().split())

arr = []
for _ in range(N):
    arr.append(int(inp()))
arr.sort()

r = arr[-1] - arr[0]
l = 1
answer = 0

while l <= r:
    mid = (l+r) // 2
    val = arr[0]
    count = 1
    for i in range(n):
        if arr[i] - val >= mid:
            val = arr[i]
            count += 1
    if count >= C:
        l = mid + 1
        answer = mid
    else:
        r = mid - 1

print(answer)
