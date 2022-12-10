from os import lseek
import sys
import heapq

inp = sys.stdin.readline

N, M = map(int, inp().split())
start = int(inp())
INF = 987654321

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    # a to b with cost c
    a, b, c = map(int, inp().split())
    graph[a].append((b, c))


def dijkstra(graph, start, distance):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    N = len(distance) - 1
    shortest_path = [[] for _ in range(N+1)]

    while queue:
        now, cost = heapq.heappop(queue)
        if distance[now] < cost:
            continue

        for node, c in graph[now]:
            if cost + c < distance[node]:
                distance[node] = cost + c
                shortest_path[node] = shortest_path[now] + [node]
                heapq.heappush(queue, (node, cost+c))

    return shortest_path


shortest_path = dijkstra(graph, start, distance)

for i in range(1, N+1):
    print(str(start) + " to " + str(i) + ": ", end="")
    if distance[i] == INF:
        print("INFINITY\n")
    else:
        print(distance[i])
        print("PATH: " + str(shortest_path[i])+"\n")
