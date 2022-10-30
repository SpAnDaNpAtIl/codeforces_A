import time
x = 'abcdgh'
n = len(x)
y = 'abedfhr'
m = len(y)
ini = time.time()
dp = [[-1 for i in range(n+1)] for j in range(m+1)]

def lcsrecursive(x,y,n,m):
    if n==0 or m==0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    if x[n-1]==y[m-1]:
        dp[m][n] = 1 + lcsrecursive(x,y,n-1,m-1)
        return dp[m][n]
    else:
        dp[m][n] = max(lcsrecursive(x,y,n-1,m), lcsrecursive(x,y,n,m-1))
        return dp[m][n]

print(lcsrecursive(x,y,n,m))