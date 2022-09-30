s = list(map(int, input().split(" ")))
n, m = s[0], s[1]
names = []
names1 = []
for i in range(m):
    s1 = input().split(" ")
    a, b = s1[0], s1[1]

    if(len(a)<=len(b)):
        names.append(a)
        names1.append(a)
    else:
        names.append(a)
        names1.append(b)

s2 = input().split(" ")
res = ''
for i in s2:
    res+=names1[names.index(i)]
    res+=' '
print(res)


