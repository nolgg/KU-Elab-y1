hs = int(input("Enter horizontal shift size: "))
vs = int(input("Enter vertical shift size: "))
# hs = 1
# vs = 2
print("Enter image:")
mainmap = []
while True:
    sub = input("")
    if sub == "-1":
        break
    mainmap.append(sub)
    sub = []


def addv(map,vs):
    if vs == 0:
        return map
    else:
        sub = []
        for i in range(vs):
            sub.append("0" * len(map[i]))
        for i in range(len(map) - vs):
            sub.append(map[i])
        return sub
    
def addh(map,hs):
    if hs <= 0:
        return map
    else:
        for j in range(len(map)):
            u = [str(k) for k in map[j]]
            sub = []
            for k in range(hs):
                    sub.append("0")
            for k in range(len(u) - hs):
                    sub.append(u[k])
            map[j] = sub
        return map
def darw(map):
    for i in map:
        for j in i:
            print(j,end="")
        print()    
print("After shift:")
addh(mainmap,hs)
darw(addv(mainmap,vs))