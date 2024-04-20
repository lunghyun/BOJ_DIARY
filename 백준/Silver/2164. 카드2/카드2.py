import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()  # queue의 가장 왼쪽 요소를 pop
    cards.append(cards.popleft())  # queue의 맨뒤로 이동
print(cards[0])