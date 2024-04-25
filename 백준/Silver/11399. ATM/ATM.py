import sys

input = sys.stdin.readline

n = int(input())
p_array = list(map(int, input().split()))

p_array.sort(reverse=True)
print(sum(p_array[i] * (i + 1) for i in range(n)))