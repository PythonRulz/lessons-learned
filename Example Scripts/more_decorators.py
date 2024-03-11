class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("Getting getter")
        return self._items

    @items.setter
    def items(self, new_items):
        print("Calling setter")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a list of items")

my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = ['pen', 'pencil', 'paper', 'notebook', 'bottl of water']
print(my_backpack.items)
my_backpack.items = 1234
