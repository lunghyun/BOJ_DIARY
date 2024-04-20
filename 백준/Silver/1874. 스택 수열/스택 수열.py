import sys

input = sys.stdin.readline

target_set = []
stack = []


def push(num, stack):
    stack.append(num)
    result.append("+")


def pop(stack):
    target_set.append(stack[-1])
    stack.pop()
    result.append("-")


n = int(input())  # n <= 10^5
target = [int(input()) for _ in range(n)]
num_array = [i for i in range(1, n + 1)]
result = []
target_idx = 0

for i in range(1, n + 1):
    while stack and target[target_idx] == stack[-1]:
        pop(stack)
        target_idx += 1
    push(i, stack)
while stack:
    pop(stack)

if target_set == target:
    for i in result:
        print(i)
else:
    print("NO")