
'''
    turtle_BJ.py (aka. version 1.1) brewed by KunToto@MikeLabDotNet [August 2024]
'''
import random, time
#import turtle

class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck
###
# test_turtle_deck(True)
###
#--------------------------------------------------------------------------------------
# put your additional class or def (aka., utilities) here
# for example,
# class myCards:
#     ''' myCard(): ลิสเก็บไพ่ที่ผู้เล่นถืออยู่ '''
#     pass
#
# def print_result(com, player, com_score, player_score):
#     pass
#--------------------------------------------------------------------------------------
def calculate(c):
    score = 0
    A_count = 0
    possible = []
    c = [str(k) for k in c]
    for i in c:
        if i[0] == "A":
            A_count += 1
        elif i[0] in ["Q","J","K","T"]:
            score += 10
        else:
            score += int(i[0])
    if A_count > 0:
        
        possible.append(score + 11)
        possible.append(score + 1)
        for i in range(A_count - 1):
            i = i + 1
            possible.append(score + 11 + i)
            possible.append(score + 1 + i)
        while True:
            a = max(possible)
            if a <= 21 or len(possible) <= 1:
                break
            else:
                possible.remove(a)
        return a
    return score

def show(player,list_card,start=False):
    list_card = [str(k) for k in list_card]
    if start:
        return str(" " * (9 - len(player)) +player + ': ' + " ".join(list_card) + " "*(16 - (len(list_card) * 2) - (len(list_card)-1)) + '-> ' + str(calculate([list_card[1]])))
    
    return str(" " * (9 - len(player)) +player + ': ' + " ".join(list_card) + " "*(16 - (len(list_card) * 2) - (len(list_card)-1)) + '-> ' + str(calculate(list_card)))
    





#---------------------------------------------------------------------------------------
def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    #----------------------
    #----------------------
    ###-------------- student code begins here --------------###

    # print(playerhand,"=",calculate([str(k) for k in playerhand]))
    # print(computerhand,"=",calculate([str(k) for k in computerhand]))
    result = ''
    playerbj = False
    computerbj = False
    player_s = 0
    computer_s = 0
    temp = 0
    computerhand = [deck.get_card()]
    playerhand = [deck.get_card()]
    computerhand.append(deck.get_card())
    playerhand.append(deck.get_card())
    computer_start = [str(k) for k in computerhand]
    ico = computer_start[0][1]
    computer_start[0] = 'O'+ ico

    print(show(player1,computer_start,True))
    computer_s = calculate(computerhand)
    print(show(player2,playerhand))
    player_s = calculate(playerhand)
        
    if player_s < 21:
        while True:
            if input('Draw another card (y/n): ').lower() == 'y':
                playerhand.append(deck.get_card())
                player_s = calculate(playerhand)
            else: break
            print(show(player2,playerhand))
            if player_s >= 21 or len(playerhand) >= 5:
                break
        if player_s <= 21 and len(playerhand) >= 5 or (player_s == 21 and len(playerhand) == 2):
            player_s = 21
            playerbj = True
    print('+++++++++++++++++++++++++++++++++')
    while True:
        if player_s <= 21:
            if (computer_s <= 16 or computer_s < player_s) and computer_s < 21 and len(computerhand) < 5:
                computerhand.append(deck.get_card())
                computer_s = calculate(computerhand)
            else: break
        elif player_s > 21:
            if computer_s <= 16 and computer_s < 21 and len(computerhand) < 5:
                computerhand.append(deck.get_card())
                computer_s = calculate(computerhand)
            else: break
    print(show(player1,computerhand))
    print(show(player2,playerhand))
    
    if player_s <= 21 and len(playerhand) >= 5 or (player_s == 21 and len(playerhand) == 2):
        player_s = 999
        playerbj = True
    elif player_s > 21:
        player_s = -999
    

    if (computer_s <= 21 and len(computerhand) >= 5) or (computer_s == 21 and len(computerhand) == 2):
        computer_s = 999
        computerbj = True
    elif computer_s > 21:
        computer_s = -999

    if (playerbj and computerbj) or (computer_s == player_s):
        result = 'Draw!'
    elif (player_s > computer_s) or playerbj:
        result = f'{player2} wins.'
    else:
        result = f'{player1} wins.'
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(result)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')

    ###--------------- student code ends here ---------------###
## main begins here
def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()

