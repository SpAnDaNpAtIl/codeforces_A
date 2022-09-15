lis=[]
for i in range(2):
    s = input().lower()
    lis.append(s)

if(len(list(set(lis)))==1):
    print(0)
else:
    if(lis[0]<lis[1]):
        print(-1)
    else:
        print(1)

