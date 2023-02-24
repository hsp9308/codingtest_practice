# 정렬된 배열에서 특정 수의 개수 구하기
# python의 bisect를 사용하지 않고 직접 이진탐색을 구현하고자 했음.
N, x = map(int, input().split())

arr = list(map(int, input().split()))

l, r = 0, N-1

if x < arr[0] or x > arr[-1]:
    print(-1)
else:
    # left-side search
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    lind = l

    l, r = 0, N-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1

    rind = r
    if lind == N or rind-lind+1 == 0:
        print(-1)
    else:
        print(rind-lind+1)
