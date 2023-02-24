# 숨바꼭질
import sys
import heapq
inp = sys.stdin.readline

N, M = map(int, inp().split())

graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    a, b = map(int, inp().split())
    graph[a].append(b)
    graph[b].append(a)

# dijkstra
q = []
heapq.heappush(q, (0, 1))
while q:
    d, now = heapq.heappop(q)
    if visited[now] != -1:
        continue
    visited[now] = d
    for node in graph[now]:
        if visited[node] == -1:
            heapq.heappush(q, (d+1, node))
ans2 = max(visited)
ans1 = visited.index(ans2)
ans3 = visited.count(ans2)
print(ans1, ans2, ans3)
