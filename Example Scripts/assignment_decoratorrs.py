class BouncyBall:
     
    def __init__(self, price, size, brand):
            self._price = price 
            self._size = size 
            self._brand = brand
            
    ## Getter/Setter _price
    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance (new_price, float) and new_price > 0.0:
            self._price = new_price
        else:
            print(f"Enter a valid price")

    ## Getter/Setter _price
    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance (new_size, str):
            self._size = new_size
        else:
            print(f"Enter a valid size")
    ## Getter/Setter _price
    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance (new_brand, str):
            self._brand = new_brand
        else:
            print(f"Enter a valid brand")

        
#############################################
            ## property() ##

class BouncyBall2:

    def __init__(self, price, size, brand):
            self._price = price 
            self._size = size 
            self._brand = brand
            
    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance (new_price, float) and new_price > 0.0:
            self._price = new_price
        else:
            print(f"Enter a valid price")

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance (new_size, str):
            self._size = new_size
        else:
            print(f"Enter a valid size")

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance (new_brand, str):
            self._brand = new_brand
        else:
            print(f"Enter a valid brand")

    price = property(get_price, set_price)
    size = property(get_size, set_size)
    brand = property(get_brand, set_brand)
#############################################
            ## @property ##
    
class BouncyBall3:

    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance (new_price, float) and new_price > 0.0:
            self._price = new_price
        else:
            print(f"Enter a valid price")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance (new_size, str):
            self._size = new_size
        else:
            print(f"Enter a valid size")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance (new_brand, str):
            self._brand = new_brand
        else:
            print(f"Enter a valid brand")
        
#################################################
            
            ## Getters and Setters Class BouncyBall ##

print('******Using Setters and Getters******\n')
new_ball = BouncyBall(1.50, 'M', 'Nike')
print(f"${new_ball.get_price()}\n{new_ball.get_size()}\n{new_ball.get_brand()}\n")

new_ball.set_price(2.25)
new_ball.set_size('L')
new_ball.set_brand('Spalding')
print(f"${new_ball.get_price()}\n{new_ball.get_size()}\n{new_ball.get_brand()}\n")

#################################################
            ## Property() BouncyBall 2 ##

print('******Using property()******\n')
new_ball2 = BouncyBall2(3.55, 'L', 'MaxFli')
print(f"${new_ball2.price}\n{new_ball2.size}\n{new_ball2.brand}\n")
new_ball2.price = 4.25
new_ball2.size = 'S'
new_ball2.brand = 'ProMax'
print(f"${new_ball2.price}\n{new_ball2.size}\n{new_ball2.brand}\n")

#################################################
            ## @property BouncyBall 3 ##

print('******Using @property******\n')
new_ball3 = BouncyBall3(4.25, 'XXS', 'MaxFli')
print(f"${new_ball3.price}\n{new_ball3.size}\n{new_ball3.brand}\n")
new_ball3.price = 6.35
new_ball3.size = 'XXL'
new_ball3.brand = 'ProGlide'
print(f"${new_ball3.price}\n{new_ball3.size}\n{new_ball3.brand}\n")




