inu = str(input()).split(' ')
n = int(inu[0])
m = int(inu[1])
a = int(inu[2])

if(n%a==0):
    i = int(n/a)
else:
    i = int(n/a)+1

if(m%a==0):
    j = int(m/a)
else:
    j = int(m/a)+1


print(i*j)