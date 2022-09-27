n = int(input())
s = list(map(int, input().split(" ")))

res = s.count(4)
one = s.count(1)
two = s.count(2)
three = s.count(3)
res+=three #three done
one = one - three if one>three else 0
res+=int(two/2)
two = (two+2)%2
if(two==0 and one==0):
    None
if(two==1 and one==0):
    res+=1
if(two==0 and one!=0):
    if(one<=4):
        res += 1
    else:
        res+=int(one/4)
        if((one+4)%4!=0):
            res+=1
if(two==1 and one!=0):
    res += 1
    if(one<=2):
        None
    else:
        res+=int((one-2)/4)

print(res)

