import sys
from collections import deque
input = sys.stdin.readline

# BFS (이어져 있는 영역 개수 세기)
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))
    

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1  # x, y 가 뒤집혀 있는 이유는 문제에서 x가 가로, y가 세로이기 때문
    
    for j in range(m):
        for k in range(n):
            if graph[k][j] == 1:
                cnt += 1
                BFS(j, k)
    print(cnt)