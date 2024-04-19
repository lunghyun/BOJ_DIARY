import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break