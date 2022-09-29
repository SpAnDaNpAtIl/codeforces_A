n = int(input())
s = list(map(int, input().split(" ")))
m = int(input())
q = list(map(int, input().split(" ")))

for i in q:
    maxi=len(s)
    while(True):
        low = sum(s[:int(maxi/2)])
        print(i, low)
        if(low==i):
            print(int((maxi)/2)+1)
            break
        elif(low<i):
            ini = int(maxi)/2
        else:
            maxi /=2

