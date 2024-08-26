class Coin:
    def __init__(self, value = 1):
        self.value = value
        self.coin_10 = 0
        self.coin_5 = 0
        self.coin_2 = 0
        self.coin_1 = 0

    def __str__(self):
        pass

    def startchange(self):
        value = self.value
        if self.value >= 10:
            self.coin_10 += value // 10
            value = value % 10
        if value >= 5:
            self.coin_5 += value // 5
            value = value % 5
        if value >= 2:
            self.coin_2 += value // 2
            value = value % 2
        if value >= 1:
            self.coin_1 += value // 1
            value = 0

    def __str__(self):
        total = ""
        if self.coin_10 > 0:
            total += f"You get {self.coin_10} of 10 Baht Coin\n"
        if self.coin_5 > 0:
            total += f"You get {self.coin_5} of 10 Baht Coin\n"
        if self.coin_2 > 0:
            total += f"You get {self.coin_2} of 10 Baht Coin\n"
        if self.coin_1 > 0:
            total += f"You get {self.coin_1} of 10 Baht Coin\n"
        return total.strip()



class BankNote:
    def __init__(self, value = 0):

        self.value = value
        self.banknote_1000 = 0
        self.banknote_500 = 0
        self.banknote_100 = 0
        self.banknote_50 = 0
        self.banknote_20 = 0

    def startchage(self):
        while self.value >= 20:
            if self.value >= 1000:
                self.banknote_1000 += self.value // 1000
                self.value = self.value % 1000
            elif self.value >= 500:
                self.banknote_500 += self.value // 500
                self.value = self.value % 500
            elif self.value >= 100:
                self.banknote_100 += self.value // 100
                self.value = self.value % 100
            elif self.value >= 50:
                self.banknote_50 += self.value // 50
                self.value = self.value % 50
            elif self.value >= 20:
                self.banknote_20 += self.value // 20
                self.value = self.value % 20
            else:
                pass

    def __str__(self):
        total = ""
        if self.banknote_1000 > 0:
            total += f"You get {self.banknote_1000} of 1000 Baht Banknote\n"
        if self.banknote_500 > 0:
            total += f"You get {self.banknote_500} of 500 Baht Banknote\n"
        if self.banknote_100 > 0:
            total += f"You get {self.banknote_100} of 100 Baht Banknote\n"
        if self.banknote_50 > 0:
            total += f"You get {self.banknote_50} of 50 Baht Banknote\n"
        if self.banknote_20 > 0:
            total += f"You get {self.banknote_20} of 20 Baht Banknote\n"
        return total.strip()

    def get_leftover(self):
        return self.value  
            

amount = int(input("Input amount : "))
a = BankNote(amount)
a.startchage()
print(a)
b = Coin(a.get_leftover())
b.startchange()
print(b)


    
    


