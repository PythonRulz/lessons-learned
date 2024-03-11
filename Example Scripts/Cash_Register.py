class CashRegister:

    tax =.05

    def __init__(self, name):
        self.name = name
        self.products = {}
           
    def show_products(self):
        for key in self.products:
            print(key)

    def add_product(self, product, price):
        self.product = product
        self.price = price
        self.products.update({product : price})

    def remove_product(self, product):
        self.product = product
        if product in self.products.keys():
            del self.products[product]
        else:
            print(f"{product} is not in the order")

    def sub_total(self):
        sub = 0
        for value in self.products.values():
            sub += value
        return sub

    def tax(self):
        return sub * tax

    def clear_products(self):
        self.products.clear()
        
        
tax = .05     
reg1 = CashRegister("Mike")
reg1.products = {"Pizza" : 10.50, "Water" : 1.50, 'Wings' : 8.75}
reg1.show_products()
print()

reg1.add_product("Extra Cheese",.50)
reg1.show_products()
print()

reg1.remove_product('Extra Cheese')
reg1.show_products()
print()

sub_total = reg1.sub_total()
print(sub_total)
print()

total = sub_total + sub_total *.05
print(total)

reg1.clear_products()

reg1.products = {"Supreme Pizza" : 18.50, "Coke" : 1.50, 'Bread Sticks' : 3.75}

##reg1.add_product("Extra Cheese",.50)
##reg1.show_products()
##print()

reg1.remove_product('Extra Cheese')
reg1.show_products()
print()

sub_total = reg1.sub_total()
print(sub_total)
print()

total = sub_total + sub_total *.05
print(f"{total:.2f}")

reg1.clear_products()
