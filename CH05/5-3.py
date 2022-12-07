import sys

def DFS(x, y, visited):
    if x < 0 or x >= len(visited) or y < 0 or y >= len(visited[0]):
        return 0
    elif visited[x][y] == 1:
        return 0

    visited[x][y] = 1
    DFS(x+1,y,visited)
    DFS(x,y+1,visited)
    DFS(x-1,y,visited)
    DFS(x,y-1,visited)

    return 1

N, M = map(int,input().split())
 
visited = []

for i in range(N):
    visited.append(list(map(int,input())))

count = 0
for i in range(N):
    for j in range(M):
        count += DFS(i,j,visited)

print(count)

