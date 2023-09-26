T = int(input())
nlist = [2, 2, 5, 5, 3, 2, 2, 5, 5, 3]

for i in range(T):
    a, b = map(int, input().split())
    a = a%10
    if a==0:
        print(10)
    elif a==1 or a == 5 or a == 6:
        print(a)
    elif a==4 or a==9:
        if b%2==0:
            print(a**2%10)
        else:
            print(a)
    else:
        if b%4==0:
            print(a**4%10)
        else:
            b = b%4
            print(a**b%10)