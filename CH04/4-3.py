import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

# d = 0 : 북, d = 1: 동, d = 2: 남, d = 3: 서

x, y, d = map(int, inp().split())


def rotate():
    global d
    d = (d-1) % 4


maps = []
count = 1

for i in range(N):
    maps.append(list(map(int, inp().split())))
dir_dict = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
back_dict = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}

act = True
rot_cnt = 0
maps[x][y] = 2
while act:
    if rot_cnt == 4:
        dX = back_dict[d]
        nx, ny = x + dX[0], y + dX[1]
        if maps[nx][ny] == 1:
            act = False
            continue
        else:
            rot_cnt = 0
            x, y = nx, ny

    dX = dir_dict[d]
    nx, ny = x + dX[0], y + dX[1]

    if maps[nx][ny] != 0:
        rotate()
        rot_cnt += 1
        continue
    else:
        rotate()
        rot_cnt = 0
        x, y = nx, ny
        maps[nx][ny] = 2
        count += 1

print(count)
