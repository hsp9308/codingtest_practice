# 문자열 압축 (프로그래머스 60057)

def solution(key, lock):
    N = len(lock)
    M = len(key)

    def rotate_90(key):
        arr = [[0]*M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                arr[j][M-i-1] = key[i][j]
        return arr

    lock_E = [[0]*3*N for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            lock_E[N+i][N+j] = lock[i][j]

    def check(lock_E):
        for i in range(N, 2*N):
            for j in range(N, 2*N):
                if lock_E[i][j] != 1:
                    return False
        return True

    for _ in range(4):
        key = rotate_90(key)
        for i in range(N-M+1, 2*N):
            for j in range(N-M+1, 2*N):
                for k in range(M):
                    for l in range(M):
                        lock_E[i+k][j+l] += key[k][l]
                if check(lock_E):
                    return True
                for k in range(M):
                    for l in range(M):
                        lock_E[i+k][j+l] -= key[k][l]

    return False
