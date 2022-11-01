#revise this thing

a = 'abcdaf'
n = len(a)
b = 'acbcf'
m = len(b)
 #copying code from printing longest subsequence
dp = [['' for i in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif b[i-1]==a[j-1]:
            dp[i][j] = dp[i-1][j-1] + b[i-1]
        else:
            l1 = len(dp[i-1][j])
            l2 = len(dp[i][j-1])
            if l1>=l2:
                dp[i][j] = dp[i-1][j] + b[i-1]
            else:
                dp[i][j] = dp[i][j-1] + a[j-1]


for i in dp:
    print(i)

print(dp[-1][-1])






