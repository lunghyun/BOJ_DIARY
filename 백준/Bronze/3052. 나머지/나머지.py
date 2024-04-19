import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]
print(len(set(map(lambda x: x % 42, nums))))