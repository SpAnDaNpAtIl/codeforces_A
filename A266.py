n = int(input())
s = input()
sum=0
for i in range(n-1):
    if(s[i:i+2]=='RR' or s[i:i+2]=='GG' or s[i:i+2]=='BB'):
        sum+=1
print(sum)