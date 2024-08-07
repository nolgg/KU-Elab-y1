num = int(input("Enter the number of rows or columns : "))

for i in range(1,num+1):
    for j in range(num):
        x = j + i
        print("%2d" % x,end=" ")
    print()