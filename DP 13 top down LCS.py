x = 'abcdgh'
n = len(x)
y = 'abedfhr'
m = len(y)

dp = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif y[i-1]==x[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for i in dp:
    print(i)

print(dp[-1][-1])