import time

s1 = list(map(int, input().split(" ")))
a, b = s1[0], s1[1]
res = 0
unu = 0
while(True):
    res += a
    unu += a
    a = int(unu/b)
    unu = unu%b
    if(a==0):
        break

print(res)
