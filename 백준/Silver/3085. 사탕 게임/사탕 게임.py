n = int(input())
array = [list(input().rstrip()) for _ in range(n)]


def checkMax():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if array[i][j] == array[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        cnt = 1
        for j in range(n - 1):
            if array[j][i] == array[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


max_cnt = 1
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]  # 행 바꾸기
            max_cnt = max(max_cnt, checkMax())
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]  # 행 바꾸기
        if i + 1 < n:
            array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]  # 열 바꾸기
            max_cnt = max(max_cnt, checkMax())
            array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]  # 열 바꾸기
print(max_cnt)