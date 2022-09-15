n = int(input())
steps=0
lis=[5,4,3,2,1]
for i in lis:
    if(n>=i):
        steps+=int(n/i)
        n-=int(n/i)*i
print(steps)