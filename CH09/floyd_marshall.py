def floyd_marshall(distance):
    N = len(distance) - 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                distance[j][k] = min(distance[j][k],distance[j][i]+distance[i][k])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.readline
    N, M = map(int,inp().split())
    start = 1
    INF = 987654321
    distance = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        distance[i][i] = 0
    for i in range(M):
        s, d, c = map(int,inp().split())
        distance[s][d] = c

    floyd_marshall(distance)

    for i in range(1, N+1):
        for j in range(1,N+1):
            print(str(i) + " to " + str(j) + ": ", end="")
            if distance[i][j] == INF:
                print("INFINITY\n")
            else:
                print(distance[i][j])
