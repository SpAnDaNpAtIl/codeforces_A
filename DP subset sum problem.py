arr = [2,3,7,8,10]
sum=11

#find if there is a subset whose sum is 11

dp = [[0 for i in range(sum+1)] for i in range(len(arr)+1)]

dp[0] = [False for i in range(sum+1)]
for i in range(len(dp)):
    dp[i][0] = True


for i in range(len(arr)+1):
    for j in range(sum+1):
        if(i==0 or j==0):
            None
        elif(arr[i-1]<=sum):
            dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    print(i)

if dp[-1][-1]==True:
    print('subset possible')
else:
    print('subset not possible')