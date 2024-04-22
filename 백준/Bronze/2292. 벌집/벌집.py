import sys

input = sys.stdin.readline

n = int(input())

# 1                   : 1층 : 1
# 1 + 6*1             : 2층 : 2~7
# 1 + 6*1 + 6*2       : 3층 : 8~19
# 1 + 6*1 + 6*2 + 6*3 : 4층 : 20~37
# 47 -> 46 cnt1 -> 40 cnt2 -> 28 cnt3 -> 10 cnt4 -> -1 cnt5
temp = n
count = 0
while temp > 0:
    if count == 0:
        temp -= 1
    else:
        temp -= 6 * count
    count += 1
print(count)