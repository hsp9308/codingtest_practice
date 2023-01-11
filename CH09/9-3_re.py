import heapq

def dijkstra(graph,distance,start):
    queue = []
    heapq.heappush(queue,(start,0))
    distance[start] = 0
    while queue:
        now, c0 = heapq.heappop(queue)
        if c0 > distance[now]:
            continue
        for node, c in graph[now]:
            cost = c + c0
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue,(node,cost))

import sys
inp = sys.stdin.readline
N, M, C = map(int,inp().split())

INF = 987654321
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int,inp().split())
    graph[a].append((b,c))

dijkstra(graph,distance,C)

max_cost = 0
cnt = 0
for i in range(1,N+1):
    if 0 < distance[i] < INF:
        cnt += 1
        max_cost = max(distance[i],max_cost)

print(cnt,max_cost)
