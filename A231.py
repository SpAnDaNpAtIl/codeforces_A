n = int(input())
sum=0
for i in range(n):
    s = input().split(" ")
    s = [int(j) for j in s]
    if(s[0]+s[1]+s[2] >= 2):
        sum+=1
print(sum)
