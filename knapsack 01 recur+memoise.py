wt = [1,3,4,5]
val=  [1,4,5,7]
n = len(wt)
w= 3



def knapsack(wt, val, n, w):
    if(n==0 or w==0):
        return 0

    if(wt[n-1]<=w):
        return max(val[n-1]+knapsack(wt, val, n-1, w-wt[n-1]), knapsack(wt, val, n-1, w))
    else:
        return knapsack(wt, val, n-1, w)

print(knapsack(wt, val, n, w))