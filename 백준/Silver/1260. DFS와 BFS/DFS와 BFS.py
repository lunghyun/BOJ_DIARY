import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수, v: 시작 정점


def dfs(graph, point):  # 스택
    isVisited = [False] * (n + 1)
    isVisited[point] = True
    stack = [point]  # 방문 순서를 저장할 스택
    isVisited[point] = True
    print(point, end=" ")
    # 방문하지 않은 인접노드로 이동(이동 시 출력)
    # 인접노드가 없으면 스택에서 pop
    # 스택이 빌 때까지 반복
    while stack:
        x = stack[-1]
        check = False
        for i in range(1, 1 + n):
            if not isVisited[i] and graph[x][i]:  # 방문하지 않고, 간선이 있다면
                stack.append(i)
                isVisited[i] = True
                print(i, end=" ")
                check = True
                break
        if not check:
            stack.pop()
    print()


def bfs(graph, point):  # 큐
    isVisited = [False] * (n + 1)
    q = deque([point])  # 방문 순서를 저장할 큐
    isVisited[point] = True  # 시작 정점 방문
    while q:  # 큐가 빌 때까지
        x = q.popleft()
        print(x, end=" ")  # 큐 앞에 있는것 출력
        for i in range(1, 1 + n):
            if not isVisited[i] and graph[x][i]:  # 방문하지 않고, 간선이 있다면
                q.append(i)
                isVisited[i] = True


# n: 정점의 개수, m: 간선의 개수, v: 시작 정점
graphs = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graphs[x][y] = True
    graphs[y][x] = True

dfs(graphs, v)
bfs(graphs, v)