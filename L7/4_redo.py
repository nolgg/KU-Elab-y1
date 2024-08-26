class Coin:
    def __init__(self, value: int= 1):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} Baht Coin'

class BankNote:
    def __init__(self, value: int=20):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} Baht Banknote'

amount = int(input("Input amount : "))
banknote = [BankNote(1000),BankNote(500),BankNote(100),BankNote(50),BankNote(20)]
coins = [Coin(10),Coin(5),Coin(2),Coin(1)]

for i in range(5):
    if banknote[i].value <= amount:
        total = amount // banknote[i].value
        amount = amount % banknote[i].value
        print(f"You get {total} of {banknote[i]}")

for i in range(4):
    if coins[i].value <= amount:
        total = amount // coins[i].value
        amount = amount % coins[i].value
        print(f"You get {total} of {coins[i]}")