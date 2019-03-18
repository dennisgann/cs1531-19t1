class Item:
    # item constructor
    def __init__(self, name, price, availability, description, ingredients, tags=""):
        self._name = name
        self._price = price
        self._availability = availability
        self._description = description
        self._ingredients = ingredients
        self._tags = tags

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    
    @property
    def is_available(self):
        return self._availability
    
    @property
    def description(self):
        return self._description

    @property
    def ingredients(self):
        return self._ingredients[::]

    @property
    def tags(self):
        return self._tags[::]
        
    def __str__(self):
        return "name: {}, price: ${:.2f}, description: {}, ingredients: {}, tags: {}".format(self._name, self._price, self._description, self._ingredients, self._tags)

    def __eq__(self, other):
        # assuming order of ingredient do not matter
        try:
            # check single valued attributes
            for attr in ['_name', '_price', '_description']:
                if getattr(self, attr) != getattr(other, attr):
                    return False

            # check multi valued attributes
            for attr in ['_ingredients', '_tags']:
                if set(getattr(self, attr)) != set(getattr(other, attr)):
                    return False
        except:
            return False

        return True
