import heapq

def dijkstra(graph,distance,start):
    queue = []
    heapq.heappush(queue,(start,0))
    distance[start] = 0
    N = len(graph) - 1
    shortest_path = [[] for _ in range(N+1)]
    while queue:
        now, c0 = heapq.heappop(queue)
        if c0 > distance[now]:
            continue
        for node, c in graph[now]:
            cost = c0 + c
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue,(node,cost))
                shortest_path[node] = shortest_path[now] + [node]

    return shortest_path

if __name__ == "__main__":
    import sys
    inp = sys.stdin.readline
    N, M = map(int,inp().split())
    start = 1
    graph = [[] for _ in range(N+1)]
    INF = 987654321
    distance = [INF]*(N+1)
    for i in range(M):
        s, d, c = map(int,inp().split())
        graph[s].append((d,c))

    shortest_path = dijkstra(graph,distance,1)

    for i in range(1, N+1):
        print(str(start) + " to " + str(i) + ": ", end="")
        if distance[i] == INF:
            print("INFINITY\n")
        else:
            print(distance[i])
            print("PATH: " + str(shortest_path[i])+"\n")
