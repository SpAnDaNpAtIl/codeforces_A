t = int(input())
for i in range(t):
    n = int(input())
    count=0
    while(n>1):
        lent = len(str(n))
        bigNum = int(str(n)[0]*lent)
        if(bigNum>n):
            count+=int(str(n)[0])-1
        else:
            count+=int(str(n)[0])
        if(lent<=1):
            break
        n = int('9'*(lent-1))
    if(n==1):
        print(1)
    else:
        print(count)
