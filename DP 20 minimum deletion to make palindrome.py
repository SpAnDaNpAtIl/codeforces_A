s = 'aebcbda'
n = len(s)
s2 = s[::-1]
m = len(s2)

dp = [[0 for i in range(n+1)] for i in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif s2[i-1]==s[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print('Length is {}'.format(dp[-1][-1]))

#remove all others to make it palindromic
print(len(s)-dp[-1][-1])
