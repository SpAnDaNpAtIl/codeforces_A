n = int(input())
s = [int(i) for i in input().split(" ")]
s.sort()
res = ''
for i in s:
    res+=str(i)
    res+=' '
print(res[:-1])