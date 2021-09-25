n = int(input())
list = [int(i) for i in input().split()]
list.reverse()  #list反転
print(" ".join(map(str,list)))

pattern = ["S","H","C","D"]
n = int(input())
cards = [[False for j in range(13)] for i in range(4)]
for i in range(n):
    mark, num = input().split()
    num = int(num)
    cards[pattern.index(mark)][num - 1] = True
for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j+1)


n = int(input())
rooms = [[[0 for x in range(10)] for y in range(3)] for z in range(4)]
for i in range(n):
    b, f, r, v = map(int,input().split())
    rooms[b - 1][f - 1][r - 1] += v
for z in range(4):
    for y in range(3):
        print(" " + " ".join(map(str, rooms[z][y])))
    if z != 3:
        print("#"*20) 
