arr = [1, 1,2,3]
diff=1
res=0
#count diff partitions such that diff is the variable given

summ = (diff+sum(arr))//2

#copied from DP 4
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
