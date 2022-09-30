for i in range(int(input())):
    s = list(map(int, input().split(" ")))
    n, k = s[0], s[1]
    if((n-k)%2==0 and n>= k**2):
        print('YES')
    else:
        print('NO')

