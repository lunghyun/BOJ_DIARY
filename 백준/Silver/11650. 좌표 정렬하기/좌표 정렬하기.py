import sys

input = sys.stdin.readline

n = int(input())  # 10^5
arr = [list(map(int, input().split())) for _ in range(n)]

# arr.sort(x좌표 오름차순)
# if x[0] == x[1]: arr.sort(y좌표 오름차순)
arr.sort()

print("\n".join([" ".join(map(str, i)) for i in arr]))
