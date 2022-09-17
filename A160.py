n = int(input())
s = [int(i) for i in input().split(" ")]
s.sort(reverse=True)
bill=[]
while(sum(s)>=sum(bill)):
    bill.append(s.pop(0))
print(len(bill))
