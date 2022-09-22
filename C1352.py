t = int(input())
for i in range(t):
    s = list(map(int, input().split(" ")))
    n, k = s[0], s[1]
    if(k<n):
        print(k)
    else:
        if(k%(n-1)!=0):
            print(k + int(k/(n-1)))
        else:
            print(k + int(k/(n-1)) -1)

