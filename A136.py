n = int(input())
s = list(map(int, input().split(" ")))
res=''
num=1
while(num!=n+1):
    res+=str(s.index(num)+1)
    num+=1
    res+=' '
print(res)