import sys

input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
mArray = list(map(int, input().split()))

for x in mArray:
    print(1 if x in a else 0)