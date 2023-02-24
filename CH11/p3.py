# 문자열 뒤집기 (백준 1439)

# 0의 그룹의 개수와 1의 그룹의 개수를 비교해서 더 작은 수의 그룹이 있는 쪽이 정답

nums = input().rstrip()

n0 = n1 = 0

if nums[0] == '0':
    n0 += 1
else:
    n1 += 1

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i] == '0':
            n1 += 1
        else:
            n0 += 1

print(min(n0, n1))
