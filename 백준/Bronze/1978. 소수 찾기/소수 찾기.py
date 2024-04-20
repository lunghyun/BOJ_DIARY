import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def primeSet(nums):
    num = set(range(2, max(nums) + 1))
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if i in num:
            num -= set(range(i * 2, max(nums) + 1, i))
    return num

print(len(primeSet(nums) & set(nums)))
