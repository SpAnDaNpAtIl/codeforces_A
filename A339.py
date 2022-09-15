a = input().split('+')
a = [int(i) for i in a]
a.sort()
res=''
for i in a:
    res+=str(i)
    res+='+'
print(res[:-1])