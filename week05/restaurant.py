from item import Item
from menu import Menu

class RestaurantSystem:
    # restaurant sys constructor
    def __init__(self, menu=None):
        self._menu = menu or Menu() # create an empty menu if `menu` is None

    # wrapper to return the menu
    def get_menu_items(self):
        return self._menu.get_items()
