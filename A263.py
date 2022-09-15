lis =[]
row_ind=0
col_ind=0
for i in range(5):
    s = input().split(" ")
    s = [int(j) for j in s]
    lis.append(s)
    if(len(list(set(s)))==2):
        row_ind = i+1
        for j in range(len(s)):
            if s[j]!=0:
                col_ind = j+1

print(abs(row_ind-3) + abs(col_ind-3))


