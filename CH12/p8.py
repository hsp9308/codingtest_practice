# 문자열 재정렬

S = input().rstrip()

arr = sorted(list(S))

nums = set(str(i) for i in range(10))
ind = 0
for i in range(len(arr)):
    if arr[i] not in nums:
        break
    ind = i

answer = ''.join(arr[ind+1:])
N = sum(map(int, arr[:ind+1]))
print(answer + str(N))
