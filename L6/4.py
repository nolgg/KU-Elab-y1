word = input("Text: ").split()
#word = "HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO".split()

def check(word1,word2):
    x = 0
    j = 0
    
    sub = []
    for i in range(0,len(word1)):
        
        sub.append(word1[i])
        sub.append(word2[i])
        
        if sub[0] != sub[1]:
            x += 1
        j += 1
        sub = []
        
    if x > 2:
        return False
    else:
        return True

def countchain(word):
    count = 1
    count_word = 1
    a = []
    for i in range(len(word)-1):
        if check(word[i],word[i+1]) == False:
            count += 1
            a.append(count_word)
            count_word = 1
        else:
            count_word += 1
    a.append(count_word)
    return count,max(a)

a,b = countchain(word)
print(f"{a} Chain(s). Maximum length is {b} word(s).")