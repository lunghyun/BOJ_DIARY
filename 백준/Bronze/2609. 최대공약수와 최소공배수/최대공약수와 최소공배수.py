import sys

input = sys.stdin.readline


def gcd(a, b):
    result = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result


def lcm(a, b):
    print(a * b // gcd(a, b))


n, m = map(int, input().split())

print(gcd(n, m))
lcm(n, m)
