for i in range(10000):
    x = input()
    sum = 0
    if x == "0":
        break
    for d in x:
        sum += int(d)
    print(sum)


import sys
p = sys.stdin.readlines()
l = ""
for i in range(len(p)):
    l += str(p[i])
l = l.lower()
for i in "abcdefghijklmnopqrstuvwxyz":
    count = l.count(i)
    print(f"{i} : {count}")



s = input()
p = input()
ss = s * 2
if p in ss:
    print("Yes")
else:
    print("No")