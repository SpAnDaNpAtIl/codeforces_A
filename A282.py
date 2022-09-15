n = int(input())
x = 0
lis=[]
for i in range(n):
    lis.append(input())

for i in lis:
    if '+' in i:
        x+=1
    else:
        x-=1
print(x)
