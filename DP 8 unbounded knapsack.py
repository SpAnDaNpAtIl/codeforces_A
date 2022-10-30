#we can use same item multiple times
wt = [1, 3, 4, 5,6,7,8,9,10,12,13,14,15,16,17,18,19]
val = [1, 4, 5, 7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = len(wt)
#w= 6
w=26

dp = [[0 for i in range(w+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(w+1):
        if(i==0 or j==0):
            dp[i][j] = 0
        if(wt[i-1]<=j):
            dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]], dp[i-1][j]) #dp[i-1][j-wt[i-1] changed to dp[i][j-wt[i-1]
        else:
            dp[i][j] = dp[i-1][j]


print(dp[-1][-1])