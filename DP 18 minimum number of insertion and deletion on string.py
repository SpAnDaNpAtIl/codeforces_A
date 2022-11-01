#Minimum Number of Insertion and Deletion to convert String a to String b

x = 'heap'
n = len(x)
y = 'pea'
m = len(y)

#I can calculate number of elements in lcs
dp = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            None
        elif y[i-1]==x[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])



print(dp[-1][-1])

#Now all I need to do is remove remaining elements from x and add remaining elements from y
res =  len(x) - dp[-1][-1]
res+=len(y) - dp[-1][-1]
print(res)