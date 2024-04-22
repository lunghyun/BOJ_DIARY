import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    cmd = input().rstrip()
    for c in cmd:
        if c == "(":
            stack.append(c)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
    if not stack:
        print("YES")
    else:
        print("NO")