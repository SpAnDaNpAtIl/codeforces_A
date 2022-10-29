
s = list(map(int, input().split(" ")))
n, a, b, c = s[0], s[1], s[2], s[3]
res=0
def ribbon(n):
    if n==0:
        return 0

    ans=0
    for i in (a,b,c):
       if n >= i:
           ans = max(ans, 1+ribbon(n-i))
    return ans

print(ribbon(n))