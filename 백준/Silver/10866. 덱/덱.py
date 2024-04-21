import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()

# dict 로 switch 문 대체 -> lambda 함수 사용
switch = {
    "push_front": lambda x: dq.appendleft(x),  # deque의 맨 앞에 원소를 추가
    "push_back": lambda x: dq.append(x),  # deque의 맨 뒤에 원소를 추가
    "pop_front": lambda: (
        dq.popleft() if dq else -1
    ),  # deque의 맨 앞에 있는 원소를 빼고, 그 수를 출력
    "pop_back": lambda: (
        dq.pop() if dq else -1
    ),  # deque의 맨 뒤에 있는 원소를 빼고, 그 수를 출력
    "size": lambda: len(dq),  # deque에 들어있는 정수의 개수를 출력
    "empty": lambda: 0 if dq else 1,  # deque이 비어있으면 1, 아니면 0을 출력
    "front": lambda: dq[0] if dq else -1,  # deque의 맨 앞에 있는 정수를 출력
    "back": lambda: dq[-1] if dq else -1,  # deque의 맨 뒤에 있는 정수를 출력
}

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        print(switch[cmd[0]]())
    else:
        switch[cmd[0]](int(cmd[1]))