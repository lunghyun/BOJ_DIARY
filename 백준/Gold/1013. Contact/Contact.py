import re

tCase = int(input()) 
output = []
for i in range(tCase):
    x = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(x)
    if m:
          output.append("YES")
    else:
          output.append("NO") 
for i in output:
      print(str(i))

#(100+1+ | 01)+ = {01, 1001, ..}
# + : 바로 앞으 문자가 1번 이상 등장
# | : or과 동일