# 못생긴 수

n = int(input())
d = [0] * n
d[0] = 1

i2 = i3 = i5 = 0

n2, n3, n5 = 2, 3, 5
for ind in range(1, n):
    d[ind] = min(n2, n3, n5)
    if d[ind] == n2:
        i2 += 1
        n2 = d[i2] * 2
    if d[ind] == n3:
        i3 += 1
        n3 = d[i3] * 3
    if d[ind] == n5:
        i5 += 1
        n5 = d[i5] * 5
print(d[-1])
