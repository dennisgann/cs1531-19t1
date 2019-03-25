from abc import ABC, abstractmethod # ABC = abstract base class

# abstract Shape Class
class Shape(ABC):
    # common attribute colour
    def __init__(self, colour):
        self._colour = colour
    
    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour

    def __str__(self):
        return self._colour

    # abstract methods to be implemented by concrete classes
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def scale(self, ratio):
        pass

# concrete Rectangle class, implements Shape
class Rectangle(Shape):
    def __init__(self, colour, width, height):
        super().__init__(colour)
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    # implement methods area & scale
    def area(self):
        return self._height * self._width
    
    def scale(self, ratio):
        self._height *= ratio
        self._width *= ratio

    def __str__(self):
        return super().__str__() + " rectangle with area {0}".format(self.area())

# concrete Circle class, implements Shape
class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    # implement methods area & scale
    def area(self):
        return 3.14 * self._radius * self._radius
    
    def scale(self, ratio):
        self._radius *= ratio

    def __str__(self):
        return super().__str__() + " circle with area {0}".format(self.area())


shape1 = Rectangle('red',5,6)
shape2 = Circle('blue',4)

print(shape1)
print(shape2)
