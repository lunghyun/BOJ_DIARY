import sys

input = sys.stdin.readline

alphabets = [-1] * 26

s = input().rstrip()

index = 0
for i in s:
    if alphabets[ord(i) - 97] == -1:
        alphabets[ord(i) - 97] = index
    index += 1
for i in alphabets:
    print(i, end=" ")