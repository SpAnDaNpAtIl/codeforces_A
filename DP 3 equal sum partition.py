arr = [1,5,11,5]
#check if we can partition this in 2 subsets so that their sums are equal
#output true or false

#total sum of array should be even for it to be distributed into equal sums
sumarray=sum(arr)
if sumarray%2!=0:
    print('Not possible')
else:
    #find a subset whose sum will be 0/5*sumarray so that remaining subset will automaticall have same sum
    summ = sumarray//2
    dp = [[0 for i in range(summ+1)] for j in range(len(arr)+1)]

    dp[0] = [False for i in range(summ+1)]
    for i in range(len(dp)):
        dp[i][0]=True




    for i in range(len(arr)+1):
        for j in range(summ+1):
            if i==0 or j==0:
                None
            elif(arr[i-1]<=summ):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    for i in dp:
        print(i)
    if(dp[-1][-1]==True):
        print('Possible')

