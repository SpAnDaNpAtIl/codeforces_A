firs = input().split(" ")
k = int(firs[-1])

sec = input().split(" ")
sec = [int(i) for i in sec]
adv = sec[k-1]
count = 0
for i in sec:
    if(i >= adv and i > 0):
        count+=1
print(count)