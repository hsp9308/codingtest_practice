import time
cache = [0]*200

def fibo(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]


def fibo_recursive(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

start = time.time()
N = 35
res_1 = []
res_2 = []
for i in range(N):
    res_1.append( fibo_recursive(i))
end = time.time()
print('Recursive: time elapsed: ', end-start, "sec")

start = time.time()    
for i in range(N):
    res_2.append( fibo(i))
end = time.time()
print('DP       : time elapsed: ', end-start, "sec")

