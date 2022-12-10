import sys
inp = sys.stdin.readline

# N, M : node number, edge number
N, M = map(int, inp().split())
INF = 987654321

# Distance information -> 2D array
distances = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    distances[i][i] = 0

for _ in range(M):
    a, b, c = map(int, inp().split())
    distances[a][b] = c


def Floyd_Marshall(distances):
    N = len(distances)-1
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                distances[j][k] = min(distances[j][k],
                                      distances[j][i]+distances[i][k])

    return


Floyd_Marshall(distances)

for i in range(1, N+1):
    for j in range(1, N+1):
        print(distances[i][j], end=" ")
    print()
    '''
        print(str(i) + " to " + str(j) + ": ", end="")
        if distances[i] == INF:
            print("INFINITY")
        else:
            print(distances[i][j])
        '''
