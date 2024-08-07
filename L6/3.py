x_grid,y_grid = [int(m) for m in input("Grid Size: ").split()]
mine = int(input("Number of mine(s): "))



def map(y,x):
    m = []
    sub = []
    for i in range(x):
        for j in range(y):
          sub.append(0)      
        m.append(sub)
        sub = []
    return m

def darwmap(map):
    for i in map:
        for j in i:
            print(j,end = " ")
        print()

def getmine(num):
    position = []
    for i in range(num):
        position.append([int(m) for m in input(f"Mine#{i+1}: ").split()])
    return position


def plantmine(y,x,map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if j == y and i == x:
                map[i][j] = "X"
    return map

def minecount(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            for x in range(-1,2):
                for y in range(-1,2):
                    if map[i][j] != "X":
                        if i - x >= 0 and j - y >= 0 and i - x < len(map) and j -y < len(map[i]):
                                if map[i-x][j-y] == "X":
                                    map[i][j] += 1
                        
    return map

mainmap = map(x_grid,y_grid)
mp = getmine(mine)
for i,k in mp:
    plantmine(i,k,mainmap)
minecount(mainmap)
darwmap(mainmap)
