n = int(input())
lis=[]
res=[False, False, False]
for i in range(n):
    s = input().split(" ")
    s = [int(j) for j in s]
    lis.append(s)

for i in range(3):
    k=1 #reference
    for j in lis:
        k+=j[i]
    if(k==1):
        res[i]=True

if(list(set(res))==[True]):
    print('YES')
else:
    print('NO')

