'''-------------------------------------------
 - Do not send this part of code!
 - No import command is allowed anywhere!
-------------------------------------------'''
def readMat(fn='L10.py\gauss01.txt'):
    m = []
    with open(fn) as fp:
        for line in fp:
            m.append(line.strip().split(' '))
    return m

def printMat(m):
    for i in range(len(m)):
        row = ''
        for j in range(len(m[0])):
            row += f'{m[i][j]:>8}'
        print(row)
    print()

# filename = 'gauss01.txt'
# m = readMat(filename)
# print(m)
'''-------------------------------------------
 END: Do not send this part of code!
-------------------------------------------'''

def format(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(m[i][j])
    return m

def format2(m):
    sub = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            sub.append(f"{m[i][j]:.0f}")
    return sub

def getRdiv(num_list, n):
    sub = []
    for i in num_list:
        if i % n == 0:
            sub.append(int(i / n))
        else:
            temp1 = i
            temp2 = n
            for j in range(n - 1, 1, -1):
                if temp1 % j == 0 and temp2 % j == 0:
                    temp1 = temp1 / j
                    temp2 = temp2 / j
                else:
                    continue
            sub.append(f"{temp1}/{temp2}")
    return sub

def getRmuli(num_list, n):
    sub = []
    for i in num_list:
        if "/" in str(i):
            temp = i.split("/")
            temp = getRdiv([temp[0] * n], temp[1])
            temp = temp[0]
            sub.append(temp)
        else:
            sub.append(i * n)
    return sub

def getRplus(num_list, n):
    sub = []
    for i in num_list:
        sub.append(i + n)
    return sub

def calR(num1, num2):
    new = []
    for i in range(len(num1)):
        for j in range(len(num2)):
            if i == j:
                if '/' in str(num1[i]) or '/' in str(num2[j]):
                    num1[i] = str(num1[i])
                    num2[j] = str(num2[j])
                    if '/' in num1[i] and '/' not in num2[j]:
                        num2[j] = f'{num2[j]}/1'
                    if '/' not in num1[i] and '/' in num2[j]:
                        num1[i] = f'{num1[i]}/1'
                    temp1 = num1[i].split('/')
                    temp2 = num2[j].split('/')
                    new.append(getRdiv([temp1[0] * temp2[0]], temp1[1] * temp2[1])[0])
                else:
                    new.append(num1[i] - num2[j])
    return new

def back_substitution(m):
    num_vars = len(m) - 1  # Number of variables
    vars_sol = [0] * num_vars  # Initialize solution list

    for i in range(num_vars - 1, -1, -1):
        total = m[i][-1]  # Start with the rightmost column value (constant term)
        for j in range(i + 1, num_vars):
            total -= m[i][j] * vars_sol[j]  # Subtract already solved variables
        vars_sol[i] = total / m[i][i]  # Solve for the current variable

    return vars_sol

# Main code for reading matrix, performing Gaussian elimination, etc.
a = readMat()
a = format(a)
print('Augmented Matrix:')
printMat(a)

count = -1
temp = []
rows = len(a)
cols = len(a[0])
alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for j in range(cols - 1):
    if j < rows:
        start_row = j
    else:
        start_row = rows - 1
    
    for i in range(start_row, rows):
        if i == j:
            temp = getRdiv(a[i], a[i][j])
            print(f'R{i + 1} => R{i + 1}/({a[i][j]})')
            count += 1
        else:
            temp = getRmuli(a[count], a[i][j])
            print(f"R{count}'->({a[i][j]})*R{count} {temp}")
            print(f"R{count + 1} ==> R{count + 1}-R{count}'")
            temp = calR(a[i], temp)
        a[i] = temp
        printMat(a)

print('Result from Gaussian Elimination:')
printMat(a)

print('After Back-Substitution:')
solutions = back_substitution(a)
for i, sol in enumerate(solutions):
    if i < len(alphalist):  # Ensure the index is within the alphalist bounds
        print(f'{alphalist[i]}: {sol:.2f}')

