input()
s = list(map(int, input().split(" ")))
s1 = [True if i%2==0 else False for i in s]

a = s1.count(True)
b = s1.count(False)
if(a>b):
    print(s1.index(False)+1)
else:
    print(s1.index(True) + 1)

