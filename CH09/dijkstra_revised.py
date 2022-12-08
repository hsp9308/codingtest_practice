import sys
import heapq
sys.stdin = open('input.txt')
inp = sys.stdin.readline
INF = 987654321

# N, M =  Node, edge number
N, M = map(int, inp().split())
# start = departure node
start = int(inp())
# graph = edge information
# ! adjacent list
# N+1 ? : node number = 1, 2, 3, ..., N
graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    # a -> b with weight cost
    a, b, cost = map(int, inp().split())
    graph[a].append((b, cost))
    # If graph is bidirectional, activate the code below
    # graph[b].append((a,cost))

# dijkstra algorithm: REVISED version
# Given start point (node), this function
# finds all shortest distances between start node
# and the others.
# Using heap structure to find the node fast with O(log(V))


def dijkstra(start, graph, distance):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    N = len(graph)-1

    while queue:
        c, now = heapq.heappop(queue)
        # if now node is already selected (= visited),
        # it is ignored.
        # (= selected one is optimized in the dijkstra algorithm)
        if distance[now] < c:
            continue
        for j in graph[now]:
            cost = c + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(queue, (cost, j[0]))


dijkstra(start, graph, distance)

for i in range(1, N+1):
    print(str(start) + " to "+str(i)+":", end=" ")
    if distance == INF:
        print("INFINITY")
    else:
        print(distance[i])
