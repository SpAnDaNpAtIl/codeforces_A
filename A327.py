n = int(input())
s = list(map(int, input().split(" ")))
max=0
if(s.count(0)==len(s)):
    print(len(s))
elif(s.count(1)==len(s)):
    print(len(s)-1)
else:
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            id=s[:i].count(1)+s[i:j+1].count(0)+s[j:].count(1)
            if(max<id):
                max=id

    print(max)
