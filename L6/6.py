x_grid,y_grid = [int(k) for k in input("City Size: ").split()]
main = []
for i in range(x_grid):
    main.append([int(k) for k in input("").split()])
# x_grid,y_grid = 4,5
# main = [[2,3,5,6,2],[1,3,4,7,1],[6,5,4,1,3],[2,3,7,9,6]]

def check_N(main):
    n = y_grid
    max = 0
    for i in range(y_grid):
        for j in range(x_grid):
            if max == 0:
                max = main[j][i]
            if main[j][i] > max:
                n += 1
                max = main[j][i]
        max = 0
    return n

def check_S(main):
    n = y_grid
    max = 0
    for i in range(y_grid-1,-1,-1):
        for j in range(x_grid-1,-1,-1):
            #print(main[j][i])
            if max == 0:
                max = main[j][i]
            if main[j][i] > max:
                n += 1
                max = main[j][i]
            # print(max)
        max = 0
    return n
def check_E(main):
    n = x_grid
    max = 0
    for j in range(x_grid):
        for i in range(y_grid-1,-1,-1):
            #print(main[j][i])
            if max == 0:
                max = main[j][i]
            if main[j][i] > max:
                n += 1
                max = main[j][i]
            #print(max)
        max = 0
    return n
def check_W(main):
    n = x_grid
    max = 0
    for j in range(x_grid):
        for i in range(y_grid):
            #print(main[j][i])
            if max == 0:
                max = main[j][i]
            if main[j][i] > max:
                n += 1
                max = main[j][i]
            #print(max)
        max = 0
    return n

def output(main):
    dic = dict()
    dic["N"] = check_N(main)
    dic["S"] = check_S(main)
    dic["E"] = check_E(main)
    dic["W"] = check_W(main)
    sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
    maxvalues = max(sorted_dic.values())
    for i,k in sorted_dic.items():
        if maxvalues == k:
            print(i,end=" ")

output(main)