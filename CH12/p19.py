# 연산자 끼워넣기 (백준 14888)

N = int(input())

nums = list(map(int, input().split()))
max_val = -int(1e+10)
min_val = int(1e+10)

add, sub, mul, div = map(int, input().split())


def dfs(i, num):
    global max_val, min_val
    global add, sub, mul, div

    if i == N:
        max_val = max(max_val, num)
        min_val = min(min_val, num)

    if add > 0:
        add -= 1
        dfs(i+1, num+nums[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, num-nums[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, num*nums[i])
        mul += 1
    if div > 0:
        div -= 1
        if num >= 0:
            dfs(i+1, num//nums[i])
        else:
            dfs(i+1, -((-num)//nums[i]))
        div += 1


dfs(1, nums[0])
print(max_val, min_val)
