n = int(input())
s = list(map(int, input().split(" ")))
count=1
res=0
for i in range(n-1):
    if s[i]<=s[i+1]:
        count+=1
    else:
        res = max(count, res)
        count=1

res = max(count, res)

print(res)