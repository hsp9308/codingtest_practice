# 만들 수 없는 금액
# 1원부터 차례대로 체크하면 되는데,
# 동전을 작은 금액부터 오름차순 정렬한 뒤
# 가장 작은 코인부터 꺼내어 비교
# answer 원에 대해 coin이 answer보다 작으면 answer원까지는 만들 수 있음
# answer += coin

N = int(input())
coins = list(map(int, input().split()))

coins.sort()

answer = 1

for c in coins:
    if answer < c:
        break
    answer += c

print(answer)
