import sys
input = sys.stdin.readline

n = int(input())
tsize = list(map(int, input().split()))
t, p = map(int, input().split())

output_t = 0
output_p = [0, 0]

for i in tsize:
    output_t += i // t
    if i % t != 0:
        output_t += 1

output_p[0] = n // p
output_p[1] = n % p

print(output_t)
print(output_p[0], output_p[1])