import sys

input = sys.stdin.readline

# 자신보다 큰 덩치의 사람이 k명이면 덩치 등수는 k+1이다.

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")