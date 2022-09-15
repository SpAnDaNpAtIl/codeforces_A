s = input().split(" ")
n, k = int(s[0]), int(s[1])

for i in range(k):
    if(n%10==0):
        n/=10
    else:
        n-=1
print(int(n))