import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

# i * 31 mod 1234567891
result = 0
for i in range(n):
    result += (ord(s[i]) - 96) * 31**i
print(result % 1234567891)
