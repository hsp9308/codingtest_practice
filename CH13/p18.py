# 괄호 변환 (프로그래머스 60058)
def make_uv(strs):
    n1 = n2 = 0
    for s in strs:
        if s == '(':
            n1 += 1
        else:
            n2 += 1
        if n1 == n2:
            break
    return strs[:n1+n2], strs[n1+n2:]


def is_correct(strs):
    stack = []
    for s in strs:
        if s == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False
    return True if not stack else False


def solution(p):
    answer = ''
    if p == '':
        return answer

    u, v = make_uv(p)
    if is_correct(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for s in u[1:-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        return answer
