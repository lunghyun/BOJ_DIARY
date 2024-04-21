import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
que = deque(range(1, n + 1))

print("<", end="")
while que:
    for _ in range(k - 1):
        que.append(que.popleft())
    print(que.popleft(), end="")
    if que:
        print(", ", end="")
print(">")
