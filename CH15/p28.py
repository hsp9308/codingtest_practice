# 고정점 찾기
# 역시 이진탐색으로 할 수 있고, 서로 다른 수로 오름차순 정렬되어 있으므로,
# 범위 설정이 용이함.
# Q. 중복된 수가 있다면 어떻게 해야하나?
import sys
inp = sys.stdin.readline

N = int(inp())
arr = list(map(int, inp().split()))

l, r = 0, N-1
if arr[0] == 0:
    print(0)
elif arr[-1] == N-1:
    print(N-1)
else:
    answer = -1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == mid:
            answer = mid
            break
        elif arr[mid] > mid:
            r = mid - 1
        else:
            l = mid + 1
    print(answer)
