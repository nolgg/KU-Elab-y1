def readMat(fn='L10.py\\gauss01.txt'):
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
                    temp1 = temp1 // j
                    temp2 = temp2 // j
            sub.append(f"{temp1}/{temp2}")
    return sub

def getRmuli(num_list, n):
    sub = []
    for i in num_list:
        if "/" in str(i):
            temp = i.split("/")
            temp = getRdiv([int(temp[0]) * n], int(temp[1]))
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
                    new.append(getRdiv([int(temp1[0]) * int(temp2[0])], int(temp1[1]) * int(temp2[1]))[0])
                else:
                    new.append(num1[i] - num2[j])
    return new

def cal2(m, n):
    if '/' not in str(m):
        m = f'{int(m)}/1'
    if '/' not in str(n):
        n = f'{int(n)}/1'
    
    m_num, m_den = map(int, m.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    numerator = m_num * n_den
    denominator = m_den * n_num
    
    if denominator == 0:
        raise ValueError("Division by zero occurred in cal2")
    
    result = getRdiv([numerator], denominator)[0]
    return result

def cal3(m, n):
    if '/' not in str(m):
        m = f'{int(m)}/1'
    if '/' not in str(n):
        n = f'{int(n)}/1'
    
    m_num, m_den = map(int, m.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    numerator = m_num * n_den + m_den * n_num
    denominator = m_den * n_den
    
    if denominator == 0:
        raise ValueError("Division by zero occurred in cal3")
    
    result = getRdiv([numerator], denominator)[0]
    return result

def is_valid_number(value):
    if isinstance(value, str):
        if value.strip() == '':
            return False
        if '/' in value:
            num, denom = value.split('/')
            return denom.isdigit() and num.isdigit()
        return value.isdigit()
    return False

# Main Code
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

formular = []
answer = []
for row in a:
    formular.append(row[:-1])  # All elements except the last one
    answer.append(row[-1])     # The last element is the answer

var = len(answer)
x = [0] * var

for i in range(var - 1, -1, -1):
    x[i] = answer[i]
    for j in range(i + 1, var):
        term = formular[i][j]
        if not is_valid_number(term):
            term = 0
        if '/' in str(term):
            x[i] = cal3(x[i], term)
        else:
            term = int(term) if term != '' else 0
            x[i] = cal3(x[i], term * x[j])
    
    x[i] = cal2(x[i], formular[i][i])

for i in range(var):
    print(f'{alphalist[i]} = {x[i]}')
