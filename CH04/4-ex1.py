N = int(input())

orders = input().split()

pos_x, pos_y = 1, 1

end_pos = N

# Better?
ord_list = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for ord in orders:
    for i in range(len(ord_list)):
        if ord == ord_list[i]:
            new_x = pos_x + dx[i]
            new_y = pos_y + dy[i]

    if new_x < 1 or new_x > N or new_y < 1 or new_y > N:
        continue
    else:
        pos_x, pos_y = new_x, new_y

'''
for ord in orders:
    if ord == 'L' and (pos_y != 1):
        pos_y -= 1
    elif ord == 'R' and (pos_y != end_pos):
        pos_y += 1
    elif ord == 'U' and (pos_x != 1):
        pos_x -= 1
    elif ord == 'D' and (pos_x != end_pos):
        pos_x += 1
'''
print(pos_x, pos_y)
