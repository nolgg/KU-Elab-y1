string = input("Text: ")
sub = input("Substring: ")
#string  = "acababababaccbabab"
#sub = "abc"

ls = len(string)
lensub = len(sub)

def check(a,sub):
    x = 0
    for i in range(lensub):
        if a[i] != sub[i]:
            x += 1
    if x == 0:
        return True
    return False

def check2(a,sub):
    x = 0
    for i in range(lensub):
        if a[i] != sub[i]:
            x += 1
    if x == 1:
        return True
    return False
def makedummy(a,sub):
    str = ""
    for i in range(lensub):
        if a[i] != sub[i]:
            str += "?"
        else:
            str += a[i]
    return str

l = 0
counter = 0
istrue = 0
m = 0
main = []
for i in range(-1,ls):
    l = i + m
    counter = 0
    str = ""
    for j in range(lensub):
        l += 1
        if l < ls:
            str += string[l]
            counter += 1
        if counter == lensub:
            if check(str,sub):
                istrue += 1
                m += lensub - 1
                main.append(f"[{str}]")
            else:
                main.append(str[0])
    if len(str) < lensub:
        main.append(str)
        
if istrue == 0:
    l = 0
    counter = 0
    istrue = 0
    m = 0
    main2 = []
    sub2 = []
    for i in range(-1,ls):
        l = i + m
        counter = 0
        str = ""
        for j in range(lensub):
            l += 1
            if l < ls:
                str += string[l]
                counter += 1
            if counter == lensub:
                if check2(str,sub):
                    m += lensub - 1
                    main2.append(f"[{makedummy(str,sub)}]")
                else:
                    main2.append(str[0])
        if len(str) <= lensub -1:
            sub2.append(str)
    main2.append(sub2[0])
    
if istrue != 0:   
    print(*main,sep = "")
else:
    print(*main2,sep="")     