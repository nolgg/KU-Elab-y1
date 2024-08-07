st = input("Input sentence: ")
row = int(input("Input row: "))
# st = "YouNeverKnewHowWonderfulThatSmileCouldMakeSomeoneFeel"
# row = 7

all_row = [""] * row
q = 0
b = -1
for i in st:
    all_row[q] += i
    if q == row-1 or q == 0:
        b = b*-1
    q += b
print("".join(all_row))