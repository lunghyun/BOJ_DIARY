import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 토마토가 있는 칸을 큐에 넣어주기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

# BFS
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

answer = 0
for i in range(n):
    for j in range(m):
        # 토마토가 모두 익지 못하는 상황
        if graph[i][j] == 0 and visited[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer, visited[i][j])

print(answer-1)