t=int(input())
pri=[]
for i in range(t):
    s = list(map(int, input().split(" ")))
    pri.append(s)

pri1 = sorted(pri, key= lambda d: d[0])
pri2 = sorted(sorted(pri, key= lambda d: d[0]), key = lambda d: d[1], reverse=True)
booler=False
count=0
for i in range(t):
    if(pri1[i]==pri2[i]):
        count+=1
    if (count == 2):
        booler = True
        break
if(booler==True):
    print('Happy Alex')
else:
    print("Poor Alex")