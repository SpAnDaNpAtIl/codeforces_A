n = int(input())
s = input()
a, d = s.count('A'), s.count('D')
if(a>d):
    print('Anton')
elif(a==d):
    print("Friendship")
else:
    print('Danik')
