#length array given with a prize for each length
length = [1,2,3,4,5,6,7,8]
#prize array representing prize for that specific length
prize = [1,5,8,9,10,17,17,20]

n=8
w=n
val = prize
wt = length

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