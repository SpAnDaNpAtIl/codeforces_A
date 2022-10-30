coins = [1,2,3]
summ=5
n = len(coins)
#coins.sort() #so that bigger coins can be obtained early when starting from last
infi = float('inf')

dp = [[0 for i in range(summ+1)] for j in range(n+1)]
dp[0] = [infi for i in range(summ+1)]
for i in range(len(dp)):
    dp[i][0] = 0

for i in range(n+1):
    for j in range(summ+1):
        if i==0 or j==0:
            None
        elif coins[i-1]<=j:
            dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    print(i)

print(dp[-1][-1])