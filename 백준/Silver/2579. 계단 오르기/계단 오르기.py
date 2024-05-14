import sys
input = sys.stdin.readline

n = int(input())
stair_score = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = stair_score[1]
if n > 1:
    dp[2] = stair_score[1] + stair_score[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + stair_score[i - 1] + stair_score[i], dp[i - 2] + stair_score[i])
print(dp[n])