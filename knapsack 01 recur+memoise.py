wt = [1, 3, 4, 5,6,7,8,9,10,12,13,14,15,16,17,18,19]
val = [1, 4, 5, 7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(len(wt)-len(val))
n = len(wt)
w = 26

dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]


def knapsack(wt, val, n, w):
    if (n == 0 or w == 0):
        return 0

    if(dp[n][w]!=-1):
        return dp[n][w]
    if (wt[n - 1] <= w):
        dp[n][w] = max(val[n - 1] + knapsack(wt, val, n - 1, w - wt[n - 1]), knapsack(wt, val, n - 1, w))
        return dp[n][w]
    else:
        dp[n][w] = knapsack(wt, val, n - 1, w)
        return dp[n][w]

import time
a = time.time()
print(knapsack(wt, val, n, w))
print(time.time()-a)