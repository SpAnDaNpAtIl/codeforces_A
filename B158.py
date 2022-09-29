n = int(input())
s = list(map(int, input().split(" ")))
s.sort(reverse=True)
res = s.count(4)
one = s.count(1)
two = s.count(2)
three = s.count(3)

res+=three
one = 0 if three>=one else one-three
three=0

if((2+two)%2==0):
    res+=two/2
    two=0
else:
    res+=int(two/2)
    two=1

if(one==0):
    if(two==0):
        None
    else:
        res+=1
        two==0
else:
    if(two==0):
        if(one%4!=0):
            res+=int(one/4)+1
            one=0
        else:
            res+=int(one/4)
            one=0
    else:
        if(one<=2):
            res+=1
            two=0
            one=0
        else:
            res+=1
            two=0
            one-=2
            if(one%4!=0):
                res += int(one / 4) + 1
                one = 0
            else:
                res += int(one / 4)
                one = 0

print(int(res))



