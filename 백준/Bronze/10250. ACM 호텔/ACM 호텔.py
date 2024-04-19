import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    try:
        h, w, n = map(int, input().split())
        floor = n % h if n % h != 0 else h
        room = n // h + 1 if n% h !=0 else n // h
        print(floor * 100 + room)
    except:
        break