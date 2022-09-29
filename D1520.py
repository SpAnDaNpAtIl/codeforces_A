from collections import Counter
t = int(input())
for i in range(t):
    input()
    s = [x - i for i,x in enumerate(map(int, input().split(" ")))]
    lis = Counter(s)
    print(s, lis)


