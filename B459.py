input()
s = list(map(int, input().split(" ")))
s.sort()
lenf = len(s)
if(s[-1]-s[0] != 0):
    print(s[-1]-s[0], s.count(s[0])*s.count(s[-1]))
else:
    print(s[-1] - s[0], int(lenf*(lenf-1)/2))