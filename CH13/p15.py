# 특정 거리의 도시 찾기 (백준 18352)
# BFS로 노드 사이의 거리를 계속 업데이트해주면 됨.
import sys
from collections import deque
inp = sys.stdin.readline

# K : distance = K
# X : 출발 노드
N, M, K, X = map(int, inp().split())


def BFS(graph, visited, start):
    q = deque()
    q.append((0, start))
    while q:
        d, now = q.popleft()
        if visited[now] != -1:
            continue
        visited[now] = d
        for node in graph[now]:
            if visited[node] == -1:
                q.append((d+1, node))


graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, inp().split())
    graph[a].append(b)
BFS(graph, visited, X)

if K not in visited:
    print(-1)
else:
    for i in range(1, N+1):
        if visited[i] == K:
            print(i)
