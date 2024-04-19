import sys

input = sys.stdin.readline

array = []
출석안함 = []

for _ in range(28):
    n = int(input())
    array.append(n)

for i in range(1, 31):
    if i not in array:
        출석안함.append(i)

for i in 출석안함:
    print(i)