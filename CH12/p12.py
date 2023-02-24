# 기둥과 보 설치 (프로그래머스 60061)
# 제거/설치 명령마다 실행했다고 가정하고
# 매번 이 구조물이 가능한지 체크하여 실행여부를 결정.
# 구조물을 set 자료구조로 저장하게끔 하면 속도가 더 빠름. (탐색에서의 속도 개선)
def solution(n, build_frame):
    answer = set()

    def possible(answer):
        for x, y, a in answer:
            if a == 0:
                if y != 0 and ((x-1, y, 1) not in answer and (x, y, 1) not in answer) and (x, y-1, 0) not in answer:
                    return False
            else:
                if (x, y-1, 0) not in answer and (x+1, y-1, 0) not in answer and ((x-1, y, 1) not in answer or (x+1, y, 1) not in answer):
                    return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:
            answer.add((x, y, a))
            if not possible(answer):
                answer.remove((x, y, a))
        else:
            answer.remove((x, y, a))
            if not possible(answer):
                answer.add((x, y, a))
    answer = list(answer)
    answer.sort(key=lambda z: (z[0], z[1], z[2]))
    return answer
