a = input().lower()
a = a.replace('a', '')
a = a.replace('o', '')
a = a.replace('y', '')
a = a.replace('e', '')
a = a.replace('u', '')
a = a.replace('i', '')
res=''
for i in a:
    res+='.'
    res+=i
print(res)