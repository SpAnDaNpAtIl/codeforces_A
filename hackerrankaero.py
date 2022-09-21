s = input()
lis = list(set(s))
lis_count = []
for i in lis:
    lis_count.append((s.count(i), i))

lis_count = sorted(lis_count, key= lambda x: (-x[0], x[1]))
for i in range(3):
    print(lis_count[i][1], lis_count[i][0])
