# 모험가 길드
# 최대 그룹을 만들기 위해서
# 최저 공포도를 가진 모험가부터 차례대로 그룹을 만들어보자.

# 나의 풀이 : 그룹원의 stack을 쌓아서
# 그룹이 형성될 조건이 만족되면 stack을 초기화했음
# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)

# answer = 0
# stack = []

# while arr:
#     stack.append(arr.pop())
#     if len(stack) >= stack[-1]:
#         answer += 1
#         stack = []
# print(answer)

# 해답 : 내림차순 정렬 후 비교

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
count = 0
for i in arr:
    count += 1
    if count >= i:
        answer += 1
        count = 0
print(answer)
