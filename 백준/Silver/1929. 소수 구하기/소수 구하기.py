import sys

input = sys.stdin.readline
m, n = map(int, input().split())


def primeSet(n):
    num = set(range(2, n + 1))
    for i in range(2, int(n**0.5) + 1):
        if i in num:
            num -= set(range(i * 2, n + 1, i))
    return num


# set은 정렬을 하지 않는다.(집합)

result = sorted(primeSet(n) - primeSet(m - 1))

for i in result:
    if i != 1:
        print(i)