#given an array, add +/- to each element to get a target sum
#find the number of ways to get the target sum
arr = [1,1,2,3]
summ = 1

#divide this arr into two subsets, one will have +ve and other negative so adding them will give sum as in diff of these 2 subsets will give count

diff = summ
p1 = (diff + sum(arr))//2

dp = [[0 for i in range(p1+1)] for j in range(len(arr)+1)]
for i in range(len(arr)+1):
    dp[i][0] = 1

for i in range(len(arr)+1):
    for j in range(p1+1):
        if i==0 or j==0:
            None
        elif arr[i-1]<=j:
            dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    print(i)

print(dp[-1][-1])
