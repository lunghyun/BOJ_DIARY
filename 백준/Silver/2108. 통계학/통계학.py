import sys

input = sys.stdin.readline


def numMean(array):
    print(round(sum(array) / n))


def numMedian(array):
    array.sort()
    print(array[n // 2])


# def numMode(nums):
#     array = nums.copy()
#     while array:
#         if len(set(array)) == len(array):  # 겹치는 값이 없음
#             if len(array) > 1:
#                 array.sort()
#                 print(array[1])
#             else:
#                 print(array[0])
#         for i, a in enumerate(set(array)):
#             array.remove(a)
# 시간 초과


def numMode(array):
    dic = dict()
    for i in array:  # 빈도수 체크
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    mx_cnt = max(dic.values())
    mx_dic = []
    for i in dic:
        # print(f"{i} 가 {dic[i]}번 나옴")
        if mx_cnt == dic[i]:
            mx_dic.append(i)
    if len(mx_dic) > 1:
        mx_dic.sort()
        print(mx_dic[1])
    else:
        print(mx_dic[0])


def numRange(array):
    print(max(array) - min(array) if array else 0)


n = int(input())  # 홀수
nums = [int(input()) for _ in range(n)]  # -4000 ~ 4000


numMean(nums)
numMedian(nums)
numMode(nums)
numRange(nums)