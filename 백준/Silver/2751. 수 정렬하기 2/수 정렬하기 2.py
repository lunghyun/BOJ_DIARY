import sys

input = sys.stdin.readline

n = int(input())  # 1,000,000
arr = [int(input()) for _ in range(n)]  # 0 ~ 1,000,000
arr.sort()  # nlogn
for i in arr:
    print(i)