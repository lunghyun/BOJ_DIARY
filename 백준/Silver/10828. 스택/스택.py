import sys

input = sys.stdin.readline

n = int(input())


def pushX(stack, x):
    stack.append(x)


def pop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def size(stack):
    print(len(stack))


def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def whichTop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


stack = []

for _ in range(n):
    command = input()
    if command[:4] == "push":
        pushX(stack, int(command.split(" ")[1]))
    elif command[:3] == "pop":
        pop(stack)
    elif command[:4] == "size":
        size(stack)
    elif command[:5] == "empty":
        empty(stack)
    elif command[:3] == "top":
        whichTop(stack)
