for i in range(int(input())):
    dollar=0
    s1 = list(map(int, input().split(" ")))
    s2 = list(map(int, input().split(" ")))
    x, y = s1[0], s1[1]
    a, b = s2[0], s2[1]
    if(b<=2*a):
        dollar+=abs(x-y)*a
        dollar+=min(s1)*b
    else:
        dollar+=(x+y)*a
    print(dollar)


