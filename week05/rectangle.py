class Rectangle:
    #Define constructor
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    # def getHeight(self):
    #     return self._height

    # def getWidth(self):
    #     return self._width
    
    # def setWidth(self, width):
    #     self._width = width

    # def setHeight(self, height):
    #     self._height = height

    def getArea(self):
        return self._width * self._height

    def __str__(self):
        return super().__str__() + " rectangle with width {0} and height {1}".format(self.width, self.height)
