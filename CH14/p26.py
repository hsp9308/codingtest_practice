# 카드 정렬하기 (백준 1715)
# heapq를 이용해서 매번 정렬할 최소 개수의 카드 셋 2개를 뽑아 업데이트해줌
import heapq
import sys
inp = sys.stdin.readline

arr = []
N = int(inp())

for _ in range(N):
    heapq.heappush(arr, int(inp()))

answer = 0
for i in range(N-1):
    val = heapq.heappop(arr)
    val += heapq.heappop(arr)
    answer += val
    heapq.heappush(arr, val)

print(answer)
