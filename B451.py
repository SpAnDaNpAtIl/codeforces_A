n = int(input())
s = list(map(int, input().split(" ")))

s2 = s.copy()
s2.sort()
count=0
booler=True
lis=[]
for i in range(len(s)):
    if(s2[i]!=s[i]):
        count+=1
        lis.append(i+1)
    if(count>2):
        if(sorted(s, reverse=True)!=s):
            print("no")
        else:
            print('yes')
            print(1, len(s))
        break
if(count==2):
    print('yes')
    print(lis[0], lis[1])
if(count==0):
    print('yes')
    print(s[0], s[0])
