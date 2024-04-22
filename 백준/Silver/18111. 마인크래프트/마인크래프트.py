import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
field = []
for _ in range(n):
    field.extend(list(map(int, input().split())))

result = []
for h in range(257):  # 256
    block = b
    time = 0
    for i in field:
        if i < h:  # 쌓을때
            time += h - i
            block -= h - i
        elif i > h:  # 제거할때
            time += 2 * (i - h)
            block += i - h
    if block >= 0:
        result.append((h, time, block))

# 시간이 적은 순으로 정렬
result.sort(key=lambda x: (x[1], -x[0]))  # nlogn
print(result[0][1], result[0][0])