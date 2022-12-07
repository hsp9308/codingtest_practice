import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

stocks = list(map(int, inp().split()))

l, r = 0, max(stocks)
res = 0

while l <= r:
    mid = (l+r) // 2
    #val = sum([x-mid if x > mid else 0 for x in stocks])
    val = 0
    for x in stocks:
        if x > mid:
            val += x - mid
    if val == M:
        res = mid
        break
    if val > M:
        res = mid
        l = mid+1
    else:
        r = mid-1

print(res)
