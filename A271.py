s = input()
n=int(s)
while(True):
    n+=1
    s = str(n)
    if(len(s)==len(set(s))):
        break

print(n)