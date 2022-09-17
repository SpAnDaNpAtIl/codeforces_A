n = int(input())
max=0
ini=0
for i in range(n):
    s = input().split(" ")
    s = [int(j) for j in s]
    ini-=s[0]
    ini+=s[1]
    if(max<ini):
        max=ini

print(max)