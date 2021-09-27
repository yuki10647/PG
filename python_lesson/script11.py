#11-A
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.f, self.a, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def pri(self):
        print(self.a)
label = list(map(int, input().split()))
oplist = list(input())
d = dice(label)
for op in oplist:
    d.play(op)
d.pri()

#11-C
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.f, self.a, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def li(self):
        return [self.a, self.b, self.c, self.d, self.e, self.f]
label = list(map(int, input().split()))
dice_base = dice(label)
label2 = list(map(int, input().split()))
for op in 'EEESEEESEEENEEENEEESEEEN':
    if dice_base.li() == label2:
        print("Yes")
        break
    dice_base.play(op)
else:
    print("No")

#11-D
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.a, self.f, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def li(self):
        return [self.a, self.b, self.c, self.d, self.e, self.f]
    def com(self, label):
        for op in 'EEESEEESEEENEEENEEESEEE':
            if self.li() == label:
                return True
            self.play(op)
        else:
            return False
n =int(input())
L = []
for i in range(n):
    label = list(map(int, input().split()))
    d = dice(label)
    for d in L:
        if d.com(label):
            break
    else:
        L.append(dice(label))
        continue
    print("No")
    break
else:
    print("Yes")