from item import Item

class Menu:
    # menu constructor
    def __init__(self):
        # create menu dict
        self._items = {}

    # add item to menu
    def add_item(self, name, price, availability, description, ingredients, tags):
        # add menu entry to dict
        self._items[name] = Item(name, price, availability, description, ingredients, tags)

    # print menu to stdout
    def print_menu(self):
        for item in self._items.keys():
            print(self.get_item(item))
    
    # get an item by name from the menu
    def get_item(self, name):
        return self._items[name]

    # get menu items
    def get_items(self):
        return self._items
        