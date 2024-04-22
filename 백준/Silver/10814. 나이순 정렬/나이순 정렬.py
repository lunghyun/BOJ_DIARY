import sys

input = sys.stdin.readline

n = int(input())  # 10^5
user = []

for _ in range(n):
    age, name = input().split()
    user.append([int(age), name])

for i in sorted(user, key=lambda x: x[0]):
    print(i[0], i[1])
