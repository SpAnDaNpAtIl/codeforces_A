#for printing number of longest palindromic subsequence I can simply reverse the string and take LCS

s = 'agbcba'
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

#seperate for length as well as string
dp = [['' for i in range(n+1)] for i in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif s2[i-1]==s[j-1]:
            dp[i][j] = dp[i-1][j-1] + s2[i-1]
        else:
            if len(dp[i-1][j])>=len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print('longest palindromic subsequence is {}'.format(dp[-1][-1]))