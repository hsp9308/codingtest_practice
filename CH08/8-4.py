N = int(input())

d = [0]*1001

MAX = 796796

d[1] = 1
d[2] = 3

for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2] * 2) % MAX

print(d[N])
