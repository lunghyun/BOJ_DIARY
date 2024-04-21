import sys

input = sys.stdin.readline

n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
temp = list(map(int, input().split()))
mArr = dict()
for i in temp:
    mArr[i] = 0

for i in nArr:
    if i in mArr:
        mArr[i] += 1

for i in temp:
    print(mArr[i], end=" ")