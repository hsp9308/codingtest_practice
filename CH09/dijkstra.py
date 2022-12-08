import sys
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
visited = [False]*(N+1)
distance = [INF]*(N+1)

for _ in range(M):
    # a -> b with weight cost
    a, b, cost = map(int, inp().split())
    graph[a].append((b, cost))
    # If graph is bidirectional, activate the code below
    # graph[b].append((a,cost))


def get_smallest_node(distance, visited):
    min_value = INF
    ind = 0
    N = len(distance)-1
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            ind = i
    return ind

# dijkstra algorithm: EASY version?
# Given start point (node), this function
# finds all shortest distances between start node
# and the others.


def dijkstra(start, graph, distance, visited):
    distance[start] = 0
    visited[start] = True
    # Nearest nodes -> update the distance!
    for j in graph[start]:
        distance[j[0]] = j[1]

    N = len(graph)-1
    # N-1 Updates are done (Start to end)
    # end = ? : we do not know
    for i in range(N-1):
        now = get_smallest_node(distance, visited)
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start, graph, distance, visited)

for i in range(1, N+1):
    print(str(start) + " to "+str(i)+":", end=" ")
    if distance == INF:
        print("INFINITY")
    else:
        print(distance[i])
