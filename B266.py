s = input().split(" ")
t = int(s[1])
t0=0
s1 = input()
while(t0<t):
    s1 = s1.replace("BG", "GB")
    t0+=1

print(s1)