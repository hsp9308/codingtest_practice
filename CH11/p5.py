# 볼링공 고르기
# 나의 풀이 : 조합의 수만 구하면 되므로,
# 각 무게에 대한 공의 개수를 구한 뒤,
# 서로 다른 무게의 공의 개수 n1, n2에 대해
# answer += n1*n2를 해주면 정답이 나온다.
# 단, 무게의 경우의 수가 겨우 1에서 10 사이 이므로,
# 리스트를 만들어 처리할 수도 있음
from collections import Counter

N, M = map(int, input().split())

balls = list(map(int, input().split()))

ball_cnt = Counter(balls)
# List로 처리
# ball_cnt = [0] * 11
# for b in balls:
#     ball_cnt[b] += 1

answer = 0

for i in range(1, 10):
    for j in range(i+1, 11):
        answer += ball_cnt[i]*ball_cnt[j]

print(answer)
