def solution(N, stages):
    answer = []
    L = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if L == 0:
            fail_rate = 0
        else:
            fail_rate = count / L
        L -= count
        answer.append((i, fail_rate))

    answer.sort(key=lambda x: -x[1])
    return [x[0] for x in answer]
