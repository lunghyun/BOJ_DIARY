import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = [(0, 0)]

while queue:
    x, y = queue.pop(0)
    if x == n - 1 and y == m - 1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
