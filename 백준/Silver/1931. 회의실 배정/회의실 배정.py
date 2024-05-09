import sys
input = sys.stdin.readline

n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간이 빠른 순서대로 정렬

count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time: # 시작 시간이 이전 회의의 끝나는 시간보다 늦거나 같다면
        count += 1
        end_time = end
        
print(count)