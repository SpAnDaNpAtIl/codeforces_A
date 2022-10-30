#length of longest common substring
a = 'aabasbjasaspandyanskas'
n = len(a)
b = 'dlqwipspandyasasbjasafdfa'
m = len(b)

dp = [[0 for i in range(n+1)] for i in range(m+1)]
maxi = 0
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif b[i-1]==a[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            maxi = max(maxi, dp[i][j])
        else:
            dp[i][j] = 0

for i in dp:
    print(i)



print(maxi)