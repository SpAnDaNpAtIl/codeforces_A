a = 'geek' #a = 'aggtab'
b = 'eke'  #b = 'gxtxayb'
n = len(a)
m = len(b)

#shortest string which after merging both strings should have both strings visible
#order is important continuity is not!!

dp = [[0 for i in range(n+1)] for i in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif a[j-1]==b[i-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs = dp[-1][-1] #longest common subsequence

res = lcs + n - lcs + m -lcs #it will have these terms plus the ones which are not included #or m+n-lcs
print(res)

#we will print this super sequence later in another code


