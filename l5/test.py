rat = '__QQ\n()">\n    '.split('\n')
hunter = ' O \n/|\\\n/ \\'.split('\n')
lion = ' /\_/\ \n( o.o )\n > ^ < '.split('\n')

# pic = (rat, hunter, lion)
# for i in pic:
#     for j in i:
#         print(j)
#     print()
p1 = input("Player1 name: ")
p2 = input("Player2 name: ")
print()
countp1 = 0
countp2 = 0
round = 1
def check(a,b):
    if a == 1 and b == 2:
        return True
    elif a == 2 and b == 3:
        return True
    elif a == 3 and b == 1:
        return True
    return False
def darw(b,c):
    sub1 = []
    sub2 = []
    sub3 = []
    k = 1
    io = 1
    for i in b:
            if k == 1:
                sub1.append(i)
                sub1.append("      ")
            elif k == 2:
                sub2.append(i)
                sub2.append("  VS  ")
            elif k == 3:
                sub3.append(i)
                sub3.append("      ")
            k += 1
    for u in c:
            if io == 1:
                sub1.append(u)
            elif io == 2:
                sub2.append(u)
            elif io == 3:
                sub3.append(u)
            io += 1
    print("".join(sub1))
    print("".join(sub2))
    print("".join(sub3))
    
while round <= 5:
    print(f"Round {round}!")
    print(f"{p1} {countp1} / {p2} {countp2}")
    c1 = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    c2 = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
    if c1 == 1:
        pic1 = rat
    elif c1 == 2:
        pic1 = hunter
    elif c1 == 3:
        pic1 = lion
        
    if c2 == 1:
        pic2 = rat
    elif c2 == 2:
        pic2 = hunter
    elif c2 == 3:
        pic2 = lion
       
    darw(pic1,pic2)

    if c1 != c2:
        if check(c1,c2):
            countp1 += 1
        else:
            countp2 += 1
            
    if countp1 >= 3:
        print()
        print(f"{p1} {countp1} / {p2} {countp2}")
        print(f"{p1} win!")
        break
    elif countp2 >= 3:
        print()
        print(f"{p1} {countp1} / {p2} {countp2}")
        print(f"{p2} win!")
        break
    round += 1
    if c1 != c2:
        print()
    
if round > 5:
    print(f"{p1} {countp1} / {p2} {countp2}")
    print("Draw!")