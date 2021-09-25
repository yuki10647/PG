print('Hello World')

va1 = input()
x = int(va1)
print(x**3)

val = input('separated by space:')
a, b = [int(i) for i in val.split()]
print(a * b, a * 2 + b * 2)

val = input('Enter sec:')
a = int(val)
b = a // 3600
c = a - b * 3600
d = c // 60
e = c % 60
print(str(b) + ':' + str(d) + ':' + str(e))