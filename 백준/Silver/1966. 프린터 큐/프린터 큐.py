import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    cnt = 1
    while queue:  # 런타임 에러 방지
        if queue[0] < max(queue):
            queue.append(queue.pop(0))
        else:
            if m == 0:
                break
            queue.pop(0)
            cnt += 1
        m = m - 1 if m > 0 else len(queue) - 1
    print(cnt)