import sys
from itertools import combinations

n = int(input())

nums = list()
for i in range(1, 11):      
      for j in combinations(range(0, 10), i):  
            j = list(j)
            j.sort(reverse=True)                     
            nums.append(int("".join(map(str, j))))
nums.sort()
try:
    print(nums[n])
except:     
      print(-1)