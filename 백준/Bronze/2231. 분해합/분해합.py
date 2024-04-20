import sys

input = sys.stdin.readline

n = int(input())  # 1,000,000


def generate(n):
    result = n
    temp = n
    for i in range(len(str(n))):
        result += temp % 10  # 1의 자리수
        temp = temp // 10
    return result


# input + input 의 각 자리수의 합 = output
def solution(n):
    for i in range(1, n):
        if generate(i) == n:
            return i
    return 0


print(solution(n))