import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        que.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(que.popleft() if que else -1)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        print(1 if not que else 0)
    elif cmd[0] == "front":
        print(que[0] if que else -1)
    elif cmd[0] == "back":
        print(que[-1] if que else -1)
