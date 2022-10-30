#LCS pattern
#15 questions of this type

#first recursive approach then recursive with memoization then top-down approach

x = 'abcdgh'
n = len(x)
y = 'abedfhr'
m = len(y)

#longest common subsequence should be abdh
#print length of this longest common subsequence
#this is not the longest common substring..substring is continuous subsequence is not...

def lcsrecursive(x,y,n,m):
    if n==0 or m==0:
        return 0
    elif x[n-1]==y[m-1]:
        return 1 + lcsrecursive(x,y,n-1,m-1)
    else:
        return max(lcsrecursive(x,y,n-1,m), lcsrecursive(x,y,n,m-1))

print(lcsrecursive(x,y,n,m))
