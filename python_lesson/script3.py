for i in range(1000):
    print("Hello World")

for i in range(10000):
 a = int(input())
 if a == 0:
    break
 print(f"Case {i+1}: {a}")

for i in range(3000):
    a, b = [int(j) for j in input().split()]
    if a == 0 and b == 0:
        break
    elif a > b:
        print(f"{b} {a}")
    else:
        print(f"{a} {b}")

a, b, c = map(int,input().split())
num = 0
for i in range(a,b+1):
    if c % i == 0:
        num += 1
print(num)


