import sys
import heapq
inp = sys.stdin.readline

N, M, C = map(int, inp().split())
INF = 987654321

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a, b, c = map(int, inp().split())
    graph[a].append((b, c))


def dijkstra(graph, start, distance):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (start, 0))

    while queue:
        now, cost = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for node, c in graph[now]:
            val = cost + c
            if val < distance[node]:
                distance[node] = val
                heapq.heappush(queue, (node, val))


dijkstra(graph, C, distance)

count = 0
max_time = 0
for i in range(1, N+1):
    if 0 < distance[i] < INF:
        count += 1
        max_time = max(distance[i], max_time)

print(count, max_time)
