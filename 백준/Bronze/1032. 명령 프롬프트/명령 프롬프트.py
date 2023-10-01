N = int(input())
arr = list(range(N))

for i in range(N):
    arr[i] = input()
    
com = arr[0]
for i in range(len(arr[0])):
    for j in range(1, N):
        if com[i] != arr[j][i]:
            com = list(com)
            com[i] = "?"
            com = ''.join(com)
            break
print(com)