datab ={}

for i in range(int(input())):
    s = input()
    if s in datab:
        datab[s]+=1
        print(s+str(datab[s]))
    else:
        datab[s]=0
        print('OK')




