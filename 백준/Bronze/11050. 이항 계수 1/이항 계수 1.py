import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # nCk


# n! / (k! * (n-k)!)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


print(int(factorial(n) / (factorial(k) * factorial(n - k))))
