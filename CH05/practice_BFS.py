import sys
from collections import deque
inp = sys.stdin.readline

# 백준 24444 문제 참고
# N, M, R : 노드 개수, 간선 개수, 시작점
# output : BFS 시행 시 각 노드의 방문 순서 출력
# 인접행렬을 써서 반복문+스택으로 처리.

N, M, R = map(int,inp().split())

adj_list = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int,inp().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

for i in range(N):
    adj_list[i].sort()

visited = [0] * N
def BFS(start):
    count = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if visited[now] == 0:
            count += 1
            visited[now] = count
        for node in adj_list[now]:
            if visited[node] == 0:
                queue.append(node)
                
    return

BFS(R-1)
for n in visited:
    print(n)
