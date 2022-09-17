s = input()
word = 'hello'
for i in s:
    if(len(word)==0):
        break
    if(i==word[0]):
        word = word.replace(i, '', 1)

if(word==''):
    print('YES')
else:
    print('NO')