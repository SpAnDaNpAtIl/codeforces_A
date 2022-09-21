s1 = list(map(int, input().split(" ")))
s2 = list(map(int, input().split(" ")))

s2.sort()
s2dis = [s2[i+1]-s2[i] for i in range(len(s2)-1)]
s2dis.append(2*(s2[0]-0))
s2dis.append(2*(s1[-1]-s2[-1]))
print(format(max(s2dis)/2, '.10f'))








