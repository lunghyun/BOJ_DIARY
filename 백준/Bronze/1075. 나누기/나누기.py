N = int(input())
F = int(input())

temp = 0

for i in range(100):
    temp = N - N%100
    temp += i
    if temp % F == 0:
        break        
        
print(str(temp)[len(str(N))-2]+str(temp)[len(str(N))-1])