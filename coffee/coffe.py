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
        self.addon = []
        self.addon_menu = ''

    def set_addon_dic(self,addon_menu):
        for i in range(len(addon_menu)):
            self.addon[addon_menu[i][0]] = 0

    def set_coffee_menu(self,coffee_menu):
        self.coffee_menu = coffee_menu

    def get_coffee_type(self,coffee_type):
        self.coffee_type = coffee_type # <= list (espresso, 1)

    def get_drinking_type(self,drinking_type_list):
        self.drnking_type = drinking_type_list[0]
        self.drinking_type_number = drinking_type_list[1]
        self.price += self.get_price(self.coffee_menu,self.coffee_type[1],self.drinking_type_number)

    def get_menu(self,coffe_menu,addon_menu):
        self.coffee_menu = coffe_menu
        self.addon_menu = addon_menu    

    def set_add_on(self, one_add_on, one_add_on_price):
        self.addon[one_add_on] += 1
        self.price += one_add_on_price

    def set_add_on2(self, one_add_on_list, one_add_on_price):
        self.price += one_add_on_price
        self.addon = one_add_on_list
        

    def get_price(self,coffee_menu,coffee_type_num,drinking_type_number):
        return int(coffee_menu[coffee_type_num - 1][drinking_type_number])


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
    
    def get_input(word,type_input = int):
        tmp = ''
        while True:
            try:
                tmp = type_input(input(word))
                break
            except: print(' ERROR: Invalid input!')
        return tmp

    def get_coffee_type(i):
        while True:
            coffee_type = get_input(f'Cup #{i+1}, please select type of coffee: ')
            if coffee_type >= 1 and coffee_type <= len(coffe_menu):
                return [coffe_menu[coffee_type-1][0],coffee_type]
            print(' ERROR: Invalid input!')

    def get_HCF(coffee_type_num):
        coffe_list = coffe_menu[coffee_type_num - 1]
        strings = []
        if int(coffe_list[1]) != 0:
            strings.append('H')
        if int(coffe_list[2]) != 0:
            strings.append('C')
        if int(coffe_list[3]) != 0:
            strings.append('F')
        return ",".join(strings)


    def check_drinking_type(drinking_type,HCF):
        if drinking_type.upper() in HCF.split(','):
            return True
        return False

    def get_drinking_type(i,coffee_type_num):
        while True:
            try: 
                if len(get_HCF(coffee_type_num).split(',')) > 1:
                    drinking_type = input(f'Cup #{i+1}, please select drinking type ({get_HCF(coffee_type_num)}): ')
                    if check_drinking_type(drinking_type,get_HCF(coffee_type_num)):
                        return [drinking_type.upper(),get_drinking_type_num(drinking_type.upper())]
                    print(' ERROR: Invalid input!')
                else:
                    drinking_type = get_HCF(coffee_type_num)[0]
                    return [drinking_type.upper(),get_drinking_type_num(drinking_type.upper())]
            except: print(' ERROR: Invalid input!')
    
    def get_drinking_type_num(HCF):
        if HCF == "H":
            return 1
        elif HCF == "C":
            return 2
        elif HCF == "F":
            return 3

    def get_addon(i):
        price = 0
        addon_list = []
        while True:
            addon_num = get_input(f'Cup #{i+1}, please select add on (enter for exit): ')
            if addon_num:
                if addon_num >= 1 and addon_num <= len(addon_menu):
                    price += int(addon_menu[addon_num - 1][1])
                    addon_list.append(addon_menu[addon_num - 1][0])
                else: print(' ERROR: Invalid input!')
            else: break
        return addon_list,price
            

    while True:
        welcome()
        name = input("Enter customer's name: ")
        CB = CustomerBill(name)
        if name == 'Good day': break
        num_coffee = get_input('How many cups of coffee to order? ',int)
        for i in range(num_coffee):
            cof = CupOfCoffee()
            cof.set_coffee_menu(coffe_menu)
            cof.set_addon_dic(addon_menu)
            cof.get_coffee_type(get_coffee_type(i))
            cof.get_drinking_type(get_drinking_type(i,cof.coffee_type[1]))
            cof.set_add_on2(get_addon(i))
            
            
            
            

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