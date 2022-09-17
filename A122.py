s = input()
n = int(s)
lis = list(set(s))
if(lis==['4', '7'] or lis==['7','4']):
    print('YES')
else:
    booler=False
    lis1 = [i for i in ['4','7']]+[i+j for i in ['4','7'] for j in ['4','7']]+[i+j+k for i in ['4','7'] for j in ['4','7'] for k in ['4','7']]
    lis1 = [int(i) for i in lis1]
    for i in lis1:
        if(i<n and n%i==0):
            booler=True
            break
    if(booler==True):
        print('YES')
    else:
        print('NO')




