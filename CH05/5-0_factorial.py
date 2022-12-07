n = int(input())

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

def factorial_serial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

print(factorial_recursive(n))
print(factorial_serial(n))
