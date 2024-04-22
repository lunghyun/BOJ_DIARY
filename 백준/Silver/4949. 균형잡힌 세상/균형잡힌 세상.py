import sys

input = sys.stdin.readline

while (s := input().rstrip()) != ".":
    stack = []
    for i in s:
        if i in "([":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
        else:
            continue
    if not stack:
        print("yes")
    else:
        print("no")
