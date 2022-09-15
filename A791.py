s = input().split(' ')
s = [int(i) for i in s]
a, b = s[0], s[1]
year=0
while(True):
    year+=1
    a*=3
    b*=2
    if(a>b):
        print(year)
        break