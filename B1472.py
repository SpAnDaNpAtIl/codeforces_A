for i in range(int(input())):
    n = int(input())
    arr= list(map(int, input().split(" ")))
    summ=sum(arr)
    if(summ%2==1):
        print("NO")
    else:
        summ = summ//2
        #knapsack with sum = half of total sum
        """
        dp = [[0 for j in range(summ+1)] for k in range(n+1)]
        dp[0] = [False for j in range(summ+1)]
        for k in range(n+1):
            dp[k][0]=True
        """

        dp = [[True]+[False for j in range(summ)]]
        for k in range(n):
            dp.append([True]+[0 for j in range(summ)])


        for j in range(n+1):
            for k in range(summ+1):
                if j==0 or k==0:
                    None
                elif(arr[j-1]<=summ and k>=arr[j-1]):
                    dp[j][k] = dp[j-1][k-arr[j-1]] or dp[j-1][k]
                else:
                    dp[j][k] = dp[j-1][k]

        if(dp[-1][-1]==True):
            print("YES")
        else:
            print("NO")