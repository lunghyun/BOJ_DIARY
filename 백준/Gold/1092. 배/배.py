import sys
n = int(sys.stdin.readline())
wLimit = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
bWeight = list(map(int, sys.stdin.readline().split()))

if max(wLimit) < max(bWeight):
    print(-1)
else:
    wLimit.sort(reverse=True)
    bWeight.sort(reverse=True)
    cnt = 0

    while bWeight:
        for i in wLimit:
            if bWeight and i < bWeight[-1]:
                continue
            for box in bWeight:
                if i >= box:
                    bWeight.remove(box)
                    break
        cnt += 1

    print(cnt)