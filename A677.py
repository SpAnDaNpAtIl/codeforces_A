h = int(input().split(" ")[1])
wid=0
s = [int(i) for i in input().split(" ")]
for i in s:
    if(i>h):
        wid+=2
    else:
        wid+=1
print(wid)