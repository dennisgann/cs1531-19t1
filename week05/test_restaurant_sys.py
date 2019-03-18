import pytest
from restaurant import RestaurantSystem
from menu import Menu
from item import Item

class TestUS1(object):
    def test_empty_menu(self):
        # arrange
        sys = RestaurantSystem()
        # act
        items = sys.get_menu_items()
        # assert
        assert len(items) == 0

    def test_single_item(self):
        # arrange
        mocha = Item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])
        menu = Menu()
        menu.add_item(mocha.name, mocha.price, mocha.is_available, mocha.description, mocha.ingredients, mocha.tags)
        sys = RestaurantSystem(menu)
        # act
        items = sys.get_menu_items()
        # assert
        assert len(items) == 1
        assert "Mocha" in items
        assert items["Mocha"] == mocha
    
    def test_multiple_items(self):
        # arrange
        menu = Menu()

        test_items = []
        test_items.append(Item("Burger", 20, True, "Delicious Beef Burger", ["Lettuce", "Tomato", "Beef"], ["nut-free"]))
        test_items.append(Item("Salad", 15, False, "Vegetable salad", ["Lettuce", "Tomato", "Cucumber"], ["nut-free", "vegan", "glutten-free"]))
        test_items.append(Item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"]))

        for item in test_items:
            menu.add_item(item.name, item.price, item.is_available, item.description, item.ingredients, item.tags)
    
        system = RestaurantSystem(menu)

        # act
        menu_items = system.get_menu_items()

        # assert
        assert len(menu_items) == 3

        for item in test_items:
            assert item.name in menu_items
            assert menu_items[item.name] == item
            