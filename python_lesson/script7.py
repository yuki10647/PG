import itertools

for i in range(10000):
    n, x = map(int,input().split())
    if n == 0 and x == 0 :
        break
    else:
        all_list = list(range(1,n + 1))
        c = itertools.combinations(all_list,3)
        c_list = list(c)
        num = 0
        for i in c_list:
            if sum(i) == x:
                num += 1
        print(num)