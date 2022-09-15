n = int(input())
lis=[]
for i in range(n):
    s = str(input())
    lis.append(s)

for s in lis:
    if(len(s)>10):
        print(s[0]+str(len(s)-2)+s[-1])
    else:
        print(s)