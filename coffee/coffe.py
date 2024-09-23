def readMenu(fn='CoffeeMenu01.txt'): # นำฟังชันนี้ไปใช้อ่านเมนูกาแฟ โดยไม่ต้องส่งซ้ำ
    with open(fn) as fd:
        return fd.read()

# นิยามคลาสทั้งสองให้สมบูรณ์ตามข้อกำหนดด้านบน นิสิตสามารถเพิ่มเติมเมธอด setter / getter และอื่นๆ จากที่กำหนดด้านบนได้ตามความเหมาะสม
class CupOfCoffee:
    pass
class CustomerBill:
    pass
############################################## นิยามเฉพาะคลาส CupOfCoffee and CustomerBill ในกล่องด้านล่างนี้

class CupOfCoffee:
    def __init__(self, coffee_type = '', drinking_type = '', price = 0):
        self.coffee_type = coffee_type
        self.drnking_type = drinking_type
        self.price = price 
        self.addon = {}
        self.coffee_menu = ''
        self.addon_menu = ''

    def set_addon(self):
        pass

    def get_menu(self,coffe_menu,addon_menu):
        self.coffee_menu = coffe_menu
        self.addon_menu = addon_menu    

    def set_add_on(self, one_add_on, one_add_on_price):
        pass


    def __repr__(self):
        strings = ''
        return strings

class CustomerBill:
    def __init__(self,name) -> None:
        self.name = name
        self.order = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.order.append(aCupOfCoffeeObject)

    def receipt(self):
        pass


############################################## Your class CupOfCoffee and CustomerBill stop here
### Note that, start from this line, there is no more `class` definition!!! ###
### จะต้องไม่มีการนิยามคลาสอื่นๆ เพิ่มเติมจากจุดนี้อีกแล้ว                               ###
### อย่าลืมนิยามเมนไดรเวอร์ runStarBUGcafe_main()                               ###
############################################## Your utility codes start here



def runStarBUGcafe_main():
    coffe_menu = [k.strip().split(',') for k in coffee_menu_CSV.strip().split('\n')]
    addon_menu = [k.strip().split(',') for k in add_on_menu_CSV.strip().split('\n')]
    def welcome():
        print('Welcome to CPE38 **StarBUG Cafe!')
        print('+++++++++++++ MENU +++++++++++++')
        print('Coffee         Hot  Cold  Frappe')
        for i,k in enumerate(coffe_menu):
            print(f'{i+1}.{k[0]:<13}{int(k[1]):>3}   {int(k[2]):>3}   {int(k[3]):>3}')
        print('++++++++++++ ADD-ON ++++++++++++')
        for i,k in enumerate(addon_menu):
            print(f'{i+1}.{k[0]:<20}{int(k[1]):>2}')
        print('++++++++++++++++++++++++++++++++')
    while True:
        pass


############################################## Your main starBUG coffee system starts here
#---------------------------------------------------------------------------------------
# main begins here <- ไม่ต้องส่งโค๊ดส่วนนี้มา เพราะยังไงหลังบ้านก็รันโค๊ดนี้เป็นคำสั่ง __main__() สุดท้าย
#---------------------------------------------------------------------------------------
#coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_filename = 'coffee/CoffeeMenu02.txt'
coffee_menu_CSV = readMenu(coffee_menu_filename)
#addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
addon_menu_filename = 'coffee/CoffeeMenuAddOn01.txt'
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main()