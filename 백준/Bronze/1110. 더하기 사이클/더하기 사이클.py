n = int(input())
temp = n
cnt = 0
temp = n
if temp == 0:
    print(1)
else:
    while(True):
        if len(str(temp))==1:
            temp = 10*temp + temp
        else:
            temp = (int(str(temp)[0]) + int(str(temp)[1]))%10 + (int(str(temp)[1]))*10
        cnt += 1
        if n == temp:
            break
    print(cnt)