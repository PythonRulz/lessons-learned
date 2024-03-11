##class Circle:
##
##    def __init__(self, radius):
##        self.radius = radius
##
##    def find_diameter(self):
##        print(f"Diameter: {self.radius * 2}\n\n")
##
##my_circle = Circle(10.1)
##print(f"Radius: {my_circle.radius}")
##my_circle.find_diameter()


class Circle:
    
    pi = 3.1416
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    # Add the method below this line
    def find_area(self):
        return (self.pi * (self.radius**2))


        
blue_circle = Circle(15, "Blue")


# Call the method with blue_circle and assign the result to the variable final_area
final_area = blue_circle.find_area()
print(final_area)

##class Backpack:
##    def __init__(self):
##        self._items = []
##
##    @property
##    def items(self):
##        return self._items
##
##    def add_mult_items(self, items):
##        for item in items:
##            self.add_item(item)
##
##    def add_item(self, item):
##        for char in item:
##            if char.isdigit():
##                print("\nValid item only please\n")
##                return
##                
##        if (item.isalpha()) or (" " in item) and (not item.isspace()):
##            self._items.append(item)
##
##    def remove_item(self, item):
##        if item in self._items:
##            self._items.remove(item)
##            return 1
##        else:
##            print("This item is not in the backpack")
##            return 0
##
##    def has_item(self, item):
##        return item in self._items
##
##    def show_items(self, sorted_list=False):
##        if sorted_list:
##            print(sorted(self._items))
##        else:
##            print(self._items)
##
##my_backpack = Backpack()
##
##print(my_backpack.items)
##my_backpack.add_mult_items(["Water Bottle", "Candy", "Sleeping Bag"])
##print(my_backpack.items)

##my_backpack = Backpack()
##
##my_backpack.add_item("Water Bottle")
##my_backpack.add_item("Sleeping Bag")
##my_backpack.add_item("Candy")
##
##print("Not Sorted:")
##my_backpack.show_items()
##
##print("Sorted:")
##my_backpack.show_items(True)

##print(my_backpack.items)
##
##my_backpack.add_item("Water Bottle")
##print(my_backpack.items)
##
##my_backpack.add_item("Sleeping Bag")
##print(my_backpack.items)
##
##has_water = my_backpack.has_item("Water Bottle")
##print(has_water)
##
##my_backpack.remove_item("Water Bottle")
##print(my_backpack.items)
##
##has_water = my_backpack.has_item("Water Bottle")
##print(has_water)
##
##my_backpack.remove_item("Sleeping Bag")
##print(my_backpack.items)




        
        
