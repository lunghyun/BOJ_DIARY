import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    sum = a**2 + b**2 + c**2
    max_num = max(a, b, c)
    if sum - max_num**2 == max_num**2:
        print("right")
    else:
        print("wrong")
