#printing first longest common subsequence

a = 'acbcdf'
b = 'abcdaddgf'
n = len(a)
m = len(b)

dp = [['' for i in range(n+1)] for i in range(m+1)]
maxi = ''
lens = len(maxi)

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif b[i-1]==a[j-1]:
            dp[i][j] = dp[i-1][j-1] + b[i-1]
            if len(dp[i][j])>lens:
                maxi = dp[i][j]
                lens = len(maxi)
        else:
            dp[i][j] = ''

for i in dp:
    print(i)

print(maxi, lens)
