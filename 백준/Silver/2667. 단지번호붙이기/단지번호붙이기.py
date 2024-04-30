import sys

input = sys.stdin.readline

n = int(input())
apart = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if apart[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))  # 단지 수 출력
ans.sort()
for i in ans:
    print(i)  # 각 단지내 집의 수 출력