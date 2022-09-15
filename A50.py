s = input().split(" ")
m, n = int(s[0]), int(s[1])

i=int(m/2)
j=n/1

if(m%2==0):
    print(int(i*j))
else:
    print(int(i*j + int(n/2)))
