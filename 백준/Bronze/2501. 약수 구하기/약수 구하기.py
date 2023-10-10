n, k = map(int, input().split())
arr = []
for i in range(n, 0, -1):
    if int(n/i) not in arr and n%i == 0:
        arr.append(int(n/i))
if len(arr) < k:
    print(0)
else:
    print(arr[k-1])