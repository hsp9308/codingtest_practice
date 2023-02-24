# 럭키 스트레이트 (백준 18406)

score = input().rstrip()
mid = len(score) // 2

n1 = sum(list(map(int, score[:mid])))
n2 = sum(list(map(int, score[mid:])))

if n1 == n2:
    print("LUCKY")
else:
    print("READY")
