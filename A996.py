n = int(input())
arr=[1,5,10,20,100]
arr.sort(reverse=True)

def summer(n, arr):
    if n==0:
        return 0
    if arr[0]<=n:
        kp = n//arr[0]
        return kp+summer(n-arr[0]*kp, arr)
    else:
        return summer(n, arr[1:])

print(summer(n,arr))
