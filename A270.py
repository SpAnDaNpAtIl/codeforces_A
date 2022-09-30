for i in range(int(input())):
    a = int(input())
    n = (360)/(180-a)
    if(int(n)==n):
        print('YES')
    else:
        print('NO')