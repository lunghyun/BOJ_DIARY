n = int(input())
arr = [num for num in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        if j**2 > i:
            break
        if arr[i] > arr[i-j**2] + 1:
            arr[i] = arr[i-j**2] + 1
print(arr[n])