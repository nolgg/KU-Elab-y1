dr = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))
main = []
for i in range(size):
    main.append(input().split())

def flip(dr,main):
    if dr == "V":
        main.reverse()
        return main
    elif dr == "H":
        for i in main:
            i.reverse()
        return main

def draw(main):
    for i in main:
        print(" ".join(i))

flip(dr,main)
print("After flip:")
draw(main)





