a = int(input())
b = int(input())
c = int(input())

lis = [[a,b,c], [a,c,b], [b,a,c], [b,c,a], [c,a,b], [c,b,a]]

i = [a,b,c]
l = i[0] + (i[1]*i[2])
m = i[0]*(i[1]+i[2])
n = i[0]*i[1]*i[2]
o = (i[0]+i[1])*i[2]
p = (i[0]+i[1]+i[2])
q = (i[0]*i[1])+i[2]
print(max(l,m,n,o,p,q))