t = int(input())
res = {}
for i in range(t):
    s = list(map(int, input().split(" ")))
    res[s[0]]=s[1]

res = dict(sorted(res.items(), key=lambda d:d[1]))

res2 = dict(sorted(res.items()))
#print(res, res2)
if(res!=res2):
    print('Not possible')
else:
    print('Possible')
    for i in res.keys():
        print('B does {}ith work then A does {}th work'.format(res[i], i))
