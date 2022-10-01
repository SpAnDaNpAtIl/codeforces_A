arr = [2,3,7,8,10]
#check if sum of any subset adds to the sum_value
#if yes print True
#if no print False
sum=10
n = len(arr)


dp = [[-1 for i in range(sum+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(sum+1):
        if(i==0):
            dp[i][j]=False
        if(j==0):
            dp[i][j]=True

        if(arr[i-1]<=j):
            dp[i][j] = dp[i-1][j-1]

print(dp)



