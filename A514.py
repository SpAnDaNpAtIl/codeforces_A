n = [int(i) for i in input()]

for i in n:
    if(i>=5):
        n[n.index(i)]=9-i

n.sort()
if(list(set(n))==[0]):
    print('9'*len(n))
else:
    res=''
    for i in n:
        if(i!=0):
            res+=str(i)
            n.pop(n.index(i))
            break
    for i in n:
        res+=str(i)
    res = int(res)
    print(res)




