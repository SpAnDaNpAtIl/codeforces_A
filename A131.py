s=input()
res=''
if(s[1:]==s[1:].upper()):
    if(s[0]==s[0].lower()):
        for i in s:
            res+=i
        print(s[0].upper()+res[1:].lower())
    else:
        print(s.lower())
else:
    print(s)