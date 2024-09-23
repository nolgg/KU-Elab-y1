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
        self.drinking_type = drinking_type
        self.full_drinking_type = ''
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
        self.drinking_type = drinking_type_list[0]
        self.full_drinking_type = self.get_full_drinking_type(self.drinking_type)
        self.drinking_type_number = drinking_type_list[1]
        self.price += self.get_price(self.coffee_menu,self.coffee_type[1],self.drinking_type_number)

    def get_full_drinking_type(self,HCF):
        HCF = HCF.upper()
        if HCF == "H":
            return "Hot"
        elif HCF == "C":
            return "Cold"
        elif HCF == "F":
            return "Frappe"

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

    def show_coffee(self):
        dt_leght = len(self.full_drinking_type)
        foo = 27 - dt_leght
        print(f"{self.full_drinking_type} {self.coffee_type[0]:<{foo}} {self.price:>3}")
        if len(self.addon) >= 1:
            for addon in self.addon:
                print(f" + {addon:<29}")

    def __repr__(self):
        if len(self.addon) >= 2:
            addons = ", ".join(self.addon[:-1]) + " and " + self.addon[-1]
            strings = f" This cup is {self.full_drinking_type.lower()} {self.coffee_type[0]} with {addons}, {self.price:,} baht."
        elif len(self.addon) == 1:
            strings = f" This cup is {self.full_drinking_type.lower()} {self.coffee_type[0]} with {self.addon[0]}, {self.price:,} baht."
        else:
            strings = f" This cup is {self.full_drinking_type.lower()} {self.coffee_type[0]} with no add on, {self.price:,} baht."
        return strings

class CustomerBill:
    def __init__(self,name) -> None:
        self.name = name
        self.order = []
        self.all_price = 0
    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.order.append(aCupOfCoffeeObject)

    def get_all_price(self):
        for cof in self.order:
            self.all_price += cof.price

    def get_this_price(self):
        return self.all_price

    def receipt(self):
        self.get_all_price()
        name_leght = len(f"Kun {self.name}'s Receipt")
        bar = (32-name_leght)//2
        print("++++++++++++++++++++++++++++++++")
        print("      CPE38 **StarBUG Cafe    ")
        print(f"{' '*bar}Kun {self.name}'s Receipt{' '*bar}")
        print("++++++++++++++++++++++++++++++++")
        print("Description                Price")
        for cof in self.order:
            cof.show_coffee()
            print()
        print(f"Total                    {self.all_price:>7,}")
        print("++++++++++++++++++++++++++++++++")
        print(" Thank you, please come back :) ")
        print("++++++++++++++++++++++++++++++++")
        print()

############################################## Your class CupOfCoffee and CustomerBill stop here
### Note that, start from this line, there is no more `class` definition!!! ###
### จะต้องไม่มีการนิยามคลาสอื่นๆ เพิ่มเติมจากจุดนี้อีกแล้ว                               ###
### อย่าลืมนิยามเมนไดรเวอร์ runStarBUGcafe_main()                               ###
############################################## Your utility codes start here



def runStarBUGcafe_main():
    coffe_menu = [k.strip().split(',') for k in coffee_menu_CSV.strip().split('\n')]
    addon_menu = [k.strip().split(',') for k in add_on_menu_CSV.strip().split('\n')]
    today_coffee_dict = {}
    def welcome():
        print('Welcome to CPE38 **StarBUG Cafe!')
        print('+++++++++++++ MENU +++++++++++++')
        print('Coffee         Hot  Cold  Frappe')
        for i,k in enumerate(coffe_menu):
            print(f'{i+1}.{k[0]:<13}{int(k[1]):>3}   {int(k[2]):>3}   {int(k[3]):>3}')
        print('++++++++++++ ADD-ON ++++++++++++')
        for i,k in enumerate(addon_menu):
            print(f'{i+1}.{k[0]:<20}{int(k[1]):>2}      ')
        print('++++++++++++++++++++++++++++++++\n')
    
    def get_input(word,type_input = int):
        tmp = ''
        while True:
            try:
                tmp = type_input(input(word))
                if tmp <= 0:
                    print(' ERROR: Invalid input!')
                else: break
            except: print(' ERROR: Invalid input!')
        return tmp
    
    def get_input2(word,type_input = int):
        while True:
            tmp = input(word)
            if tmp:
                try: 
                    tmp = type_input(tmp)
                    break
                except: print(' ERROR: Invalid input!')
            else: break
        return tmp

    def get_coffee_type(i):
        while True:
            coffee_type = get_input(f'Cup #{i+1}, please select type of coffee: ')
            if coffee_type >= 1 and coffee_type <= len(coffe_menu):
                return [coffe_menu[coffee_type-1][0],coffee_type]
            print(' ERROR: Invalid input!')

    def show_good(coffee_dict,price):
        coffee_item = coffee_dict.items()
        this = '''++++++++++++++++++++++++++++++++
      CPE38 **StarBUG Cafe    
  Report for Coffee sold today
++++++++++++++++++++++++++++++++'''     
        that = '''++++++++++++++++++++++++++++++++
       What's a good day!     
++++++++++++++++++++++++++++++++'''
        print(this)
        for k,v in coffee_item:
            cup = "cup"
            if v == 0: continue
            if v != 1:
                cup = "cups"
            print(f" {k:<24}{v} {cup}")
        print(f"\nTotal sold amount{price:>10,} baht")
        print(that)
        

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
        counter = 0
        while counter < len(addon_menu):
            addon_num = get_input2(f'Cup #{i+1}, please select add on (enter for exit): ')
            if addon_num:
                if addon_num >= 1 and addon_num <= len(addon_menu) and addon_menu[addon_num - 1][0] not in addon_list:
                    price += int(addon_menu[addon_num - 1][1])
                    addon_list.append(addon_menu[addon_num - 1][0])
                    counter += 1
                else: print(' ERROR: Invalid input!')
            else: break
        return addon_list,price
            
    def add_dict(today_dict,coffee):
        if coffee not in today_dict.keys():
            today_dict[coffee] = 1
        else:
            today_dict[coffee] += 1
        return today_dict

    def add_defalut_dict(today_dict,coffee_menu):
        for i in coffee_menu:
            today_dict[i[0]] = 0
        return today_dict
    
    total = 0
    today_coffee_dict = add_defalut_dict(today_coffee_dict,coffe_menu)
    while True:
        welcome()
        name = input("Enter customer's name: ")
        cb = CustomerBill(name)
        if name.lower() == 'good day': break
        num_coffee = get_input('How many cups of coffee to order? ',int)
        for i in range(num_coffee):
            cof = CupOfCoffee()
            cof.set_coffee_menu(coffe_menu)
            cof.get_coffee_type(get_coffee_type(i))
            cof.get_drinking_type(get_drinking_type(i,cof.coffee_type[1]))
            a,b = get_addon(i)
            cof.set_add_on2(a,b)
            print(cof)
            cb.add_ordered_coffee(cof)
            today_coffee_dict = add_dict(today_coffee_dict,cof.coffee_type[0])
        cb.receipt()
        total += cb.get_this_price()
    show_good(today_coffee_dict,total)
            
            

############################################## Your main starBUG coffee system starts here
#---------------------------------------------------------------------------------------
# main begins here <- ไม่ต้องส่งโค๊ดส่วนนี้มา เพราะยังไงหลังบ้านก็รันโค๊ดนี้เป็นคำสั่ง __main__() สุดท้าย
#---------------------------------------------------------------------------------------
#coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_filename = 'coffee/CoffeeMenu01.txt'
coffee_menu_CSV = readMenu(coffee_menu_filename)
#addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
addon_menu_filename = 'coffee/CoffeeMenuAddOn02.txt'
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main()