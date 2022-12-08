import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

arr = []

d = [10001]*(M+1)
d[0] = 0
for _ in range(N):
    val = int(inp())
    arr.append(val)

for u in arr:
    # u 원 화폐 1개에 해당하는 u원에서부터 M 원까지 경우의 수 체크
    for j in range(u, M+1):
        # j-u원이 10001이 아닐 경우, 업데이트.
        # 비교 과정이 들어감에 유의.
        # Note: u-u = 0이므로, d[j=u] = u로 초기화됨에 유의
        if d[j-u] != 10001:
            d[j] = min(d[j], d[j-u]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
