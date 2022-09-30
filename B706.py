input()
s = list(map(int, input().split(" ")))
s.sort()
q = int(input())
for i in range(q):
    m = int(input())
    l=0
    u=len(s)
    if(m<s[0]):
        print(0)
    elif(m==s[0]):
        print(1)
    else:
        mid=0
        while (u - l != 1):
            mid = (u + l) // 2
            if (s[mid] < m):
                l = mid
            elif (s[mid] == m):
                break
            else:
                u = mid
        if(s[mid]<=m):
            print(mid+1)
        else:
            print(mid)