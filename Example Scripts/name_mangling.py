class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher

    def get_num_pages(self):
        return self._num_pages

    def set_num_pages(self, pages):
        if pages > 5000:
            self._num_pages = pages
        else:
            print("Invalid number of pages")

class Dog:
    def __init__(self, name, species, age):
        self.name = name
        self.__species = species
        self.age = age

class Backpack:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    
    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Invalid radius size")

my_circle = Circle(15)
print(my_circle.get_radius())
my_circle.set_radius(-10.2)
print(my_circle.get_radius())
        
    
my_backpack = Backpack()

print(my_backpack.get_items())

#my_backpack.set_items(['pencil', 'pen', 'scissors', 'eraser'])

#print(my_backpack.get_items())

my_backpack.set_items(['pencil'])
print(my_backpack.get_items())

pita = Dog('Pita', 'mutt', 1.5)
print(pita._Dog__species)
my_book = Book("LOTR", "TOLKEIN", 3000, "LOTR-98765", "New-Line")
print(my_book.get_num_pages())
my_book.set_num_pages(4000)
print(my_book.get_num_pages())
