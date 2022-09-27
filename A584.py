s = list(map(int, input().split(" ")))
n = s[0]
t = s[1]

num=10**(n-1)
if (num % t != 0):
    res = (int(num / t) + 1) * t
else:
    res = num

if(res>=t and res%t==0 and len(str(res))==n):
    print(res)
else:
    print(-1)


