# 곱하기 혹은 더하기
# 왼쪽부터 덧셈과 곱셈 결과를 계속 비교해가며 결과 만들기

strs = list(input())
nums = [int(x) for x in strs]
answer = nums[0]

for num in nums[1:]:
    answer = max(answer*num, answer+num)

print(answer)
