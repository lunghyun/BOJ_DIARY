import sys, math

input = sys.stdin.readline

a, b, v = map(int, input().split())
current = 0

# a*n - b*(n-1) >= v
# n >= (v-b)/(a-b)
print(math.ceil((v - b) / (a - b)))