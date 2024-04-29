import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pc_pair = int(input())
pc_pairs = [list(map(int, input().split())) for _ in range(pc_pair)]
queue = deque()
queue.append(1)
cnt = set()

while queue:
    current = queue.popleft()
    rmv_pairs = []
    for pair in pc_pairs:
        if current in pair:
            rmv_pairs.append(pair)
            tmp = pair[0] if pair[1] == current else pair[1]
            queue.append(tmp)
            cnt.add(tmp)
    for i in range(len(rmv_pairs)):
        pc_pairs.remove(rmv_pairs[i])

print(len(cnt))
