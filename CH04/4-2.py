loc = input()
col_ind = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x = int(loc[1])
y = col_ind[loc[0]]

count = 0

dx = [1, 2, -1, -2, -1, -2, 1, 2]
dy = [2, 1, 2, 1, -2, -1, -2, -1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 0 and ny > 0 and nx < 9 and ny < 9:
        count += 1

print(count)
