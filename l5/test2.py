def merge(a, b):
    sub = []
    for i in a:
        sub.append(i)
    for i in b:
        sub.append(i)
    x = len(sub)**2
    if isinstance(sub[0],int):
        while x < 5000:
            for i in range(0,len(sub)-1):
                if sub[i] > sub[i+1]:
                    switch(i,i+1,sub)
            x += 1   
        return sub
    else:
        while x < 5000:
            for i in range(0,len(sub)-1):
                if ord(sub[i][0]) > ord(sub[i+1][0]):
                    switch(i,i+1,sub)
            x += 1   
        return sub
       
def switch(a,b,c):
    c[a],c[b] = c[b],c[a]
    return c

 
