s1 = list(map(int, input().split(" ")))
n, k = s1[0], s1[1]
s2 = list(map(int, input().split(" ")))
minSum = (1.5 * (10 ** 5)) ** 2
ans = 0
for i in range(n - k + 1):
    if (minSum > sum(s2[i:i + k])):
        ans = i + 1
        minSum = sum(s2[i:i + k])

print(ans)