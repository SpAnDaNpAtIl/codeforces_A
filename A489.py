n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
b = list(map(int, input().split(" ")))

a.sort()
b.sort()
count=0

for i in range(n):
    for j in range(m):
        if(abs(a[i]-b[j])<=1):
            count+=1
            m-=1
            b.pop(j)
            break

print(count)



