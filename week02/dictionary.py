'''
Another useful data type built into Python is the dictionary. Unlike a list, string or tuple whose elements can be indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.

phone = {
        ‘sam’: 97896000,
        ‘john’:9584 2384,
        ‘tom’:97268907
        }

Common list methods:
- list(d.keys()) on a dictionary returns all the keys in the dictionary.  
use the 'in' keyword to check if a particular key exists
- dict() can be used to build a dictionary from a sequence of key-value pairs
- use items() to loop through the dictionary

You are given a dictionary of fruits names and their prices ($). Add a new entry: ‘golden apple’, with a price of $42 per unit. Implement a function that does the following:

1. For each fruit in store, ask the user how many units of the fruit the user would like to purchase (in any order)
2. After the user has entered the units for every fruit, calculates the total price the user has to pay and prints this value out
'''

fruit_prices = {'bananas': 10, 'rock melons': 4, 'blueberries': 23}
fruit_prices['golden apple'] = 42

def fruit_basket(fruits):
    total = 0
    for fruit, price in fruits.items():
        count = int(input(f"How many {fruit} do you want? "))
        if count < 0:
            print("Can't have negative quantity")
            return
        print(f"Added {count} {fruit} to your basket")
        total += count * price
    print(f"TOTAL = {total}")

fruit_basket(fruit_prices)