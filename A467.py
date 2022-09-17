n = int(input())
ind=0
for i in range(n):
    s = input().split(" ")
    p, q = int(s[0]), int(s[1])
    if(q-p>=2):
        ind+=1
print(ind)