arr = [1,6,11,5]
#divide into 2 partitions such that difference of their sum is minimum

def subsetSumProblem(arr, sum): #copied from earlier code
    dp = [[0 for i in range(sum + 1)] for i in range(len(arr) + 1)]
    dp[0] = [False for i in range(sum + 1)]
    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(len(arr) + 1):
        for j in range(sum + 1):
            if (i == 0 or j == 0):
                None
            elif (arr[i - 1] <= sum):
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    if dp[-1][-1] == True:
        return True
    else:
        return False


lisSums = []
for i in range(sum(arr)+1):
    if(subsetSumProblem(arr, i)):
        lisSums.append(i)

print(lisSums, len(lisSums))
#lisSums are possible sums
mini=100
for i in lisSums[:len(lisSums)//2 +1]: #because other half will be essentially s2 only
    mini = min(mini, abs(sum(arr)-2*i))

print(mini)
