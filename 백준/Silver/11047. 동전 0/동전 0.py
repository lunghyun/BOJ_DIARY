import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # N: 동전 종류 개수, K: 가치의 합
coins = list(int(input()) for i in range(n))
cnt = 0

coins.sort(reverse=True)

for i in coins:
    if k == 0:
        break
    if i <= k:
        cnt += k // i
        k %= i

print(cnt)