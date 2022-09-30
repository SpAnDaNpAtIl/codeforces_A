s1 = input().split(" ")
s, n = int(s1[0]), int(s1[1])
lis=[]
for i in range(n):
    a = list(map(int, input().split(" ")))
    x, y = a[0], a[1]
    lis.append([x,y])

lis = sorted(sorted(lis, key=lambda d: d[1], reverse=True), key=lambda d: d[0])
booler=True
for i in lis:
    if(s<=i[0]):
        booler=False
        break
    else:
        s+=i[1]

if(booler==True):
    print('YES')
else:
    print('NO')


