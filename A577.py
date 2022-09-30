s = list(map(int, input().split(" ")))
n, x = s[0], s[1]
count=0
for i in range(n):
    if(i+1<=x and x%(i+1)==0 and x/(i+1)<=n):
        count+=1
print(count)