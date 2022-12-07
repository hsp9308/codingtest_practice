N, K = map(int, input().split())

cnt = 0

while (N != 1):
    temp = (N//K)*K
    cnt += N - temp
    N = temp

    if N < K:
        break
    N = N // K
    cnt += 1

cnt += N-1
print(cnt)
