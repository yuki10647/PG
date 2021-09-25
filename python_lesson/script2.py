val = input()
a, b = [int(i) for i in val.split()]
if a < b :
    print('a < b')
elif a > b :
    print('a > b')
elif a == b :
    print('a == b')

val = input()
a, b, c = [int(i) for i in val.split()]
if a < b < c :
    print('Yes')
else :
    print('No')

val = input()
a, b, c = [int(i) for i in val.split()]
if a > b :
    a, b = b, a
if a > c :
    a, c = c, a
if b > c :
    b, c = c, b
print(a, b, c)

val = input()
W, H, x, y, r = [int(i) for i in val.split()]
if x < 0 or y < 0 :
    print('No')
elif x + r > W or y + r > H :
    print('No')
else :
    print('Yes')