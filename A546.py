s = input().split(" ")
k, n, w = int(s[0]), int(s[1]), int(s[2])
if(n>w*(w+1)*k/2):
    print(0)
else:
    print(int(w*(w+1)*k/2 - n))