row_p = int(input("Enter Rook's row position: "))
column_p = int(input("Enter Rook's column position: "))
# row_p = 2
# column_p = 6

column_p = column_p + column_p + 2

rook_p = [row_p,column_p]

space = "-----------------"

def createmap(row_p,column_p):
    x,y = row_p,column_p
    mainmap = []
    sub = []
    for j in range(0,8):
        for i in range(0,18):
            if j == x and i == y:
                sub.append("R")
            elif i == y:
                sub.append("x")
            elif j == x and i % 2 == 0 and i != 0:
                sub.append("x")
            elif i % 2 == 0 and i != 0:
                sub.append(" ")
            elif i == 0:
                pass
            else:
                sub.append("|")
        mainmap.append(sub)
        sub = []
    return mainmap


def placeR(map):
    pass
# 0 1 2 3 4 5 6 7 8
#1+2+3+5     

def draw(map):
    for k in map:
        print(space)
        print("".join(k))
    print(space)

draw(createmap(row_p,column_p))