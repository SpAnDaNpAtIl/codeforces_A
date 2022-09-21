s1 = input().split(" ")
s, n = int(s1[0]), int(s1[1])
lis=[]
booler=True
for i in range(n):
    lis.append([int(j) for j in input().split(" ")])

lis.sort()
for i in lis:
    if i[0]>s:
        booler=False
        break
    else:
        s+=i[1]

if(booler==True):
    print('YES')
else:
    print('NO')

