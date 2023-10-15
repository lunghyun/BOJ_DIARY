n, r, c = map(int, input().split())
cnt = 0
tmp = n

while tmp >= 1:
    if r < 2**(tmp-1) and c >= 2**(tmp-1):
        c -= 2**(tmp-1)
        cnt += 2**(2*tmp)//4
    elif r >= 2**(tmp-1) and c < 2**(tmp-1):
        r -= 2**(tmp-1)
        cnt += 2**(2*tmp)*2//4
    elif r >= 2**(tmp-1) and c >= 2**(tmp-1):
        r -= 2**(tmp-1)
        c -= 2**(tmp-1)
        cnt += 2**(2*tmp)*3//4
    tmp -= 1
    
print(cnt)