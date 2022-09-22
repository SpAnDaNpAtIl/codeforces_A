s = list(map(int, input().split(" ")))
n,m,a,b = s[0], s[1], s[2], s[3]
print(min(int(n/m)*b + (n%m)*a, n*a, (int(n/m)+1)*b))