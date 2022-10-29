arr = [2,3,5,6,8,10]
summ=10

dp = [[0 for i in range(summ+1)] for j in range(len(arr)+1)]
for i in dp:
    i[0] = 1

for i in range(len(arr)+1):
    for j in range(summ+1):
        if i==0 or j==0:
            None
        elif arr[i-1]<=summ and j>=arr[i-1]: #here additional condition ensures it does not reach for -1 or last indexes
            dp[i][j] = dp[i-1][j-arr[i-1]]+dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    print(i)

print(dp[-1][-1])