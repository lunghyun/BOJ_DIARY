import sys

input = sys.stdin.readline
n = int(input())


# 재귀 함수 없이 작성하면
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if n == 0:
    print(0)
else:
    cnt = 0
    temp = factorial(n)
    while temp % 10 == 0:
        temp //= 10
        cnt += 1
    print(cnt)