import sys

input = sys.stdin.readline

n = int(input())  # 3 * 10^5
arr = [int(input()) for _ in range(n)]


def my_round(num):  # round 함수 -> 0.5일 때 짝수로 반올림함
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


arr.sort()
except_num = my_round(n * 0.15)

if n == 0:
    print(0)
else:
    arr = arr[except_num : n - except_num]
    print(my_round(sum(arr) / len(arr)))