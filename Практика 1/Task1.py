
class Rectangle:

    def __init__(self, width = 1.0, length = 1.0):
        self.__width = width
        self.__length = length

    def count_perimiter(self):
        return self.__length*2+self.__width*2

    def count_area(self):
        return self.__length*self.__width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if (0.0<length<20.0) and type(length) is float:
            self.__length=length
        else:
            print("Invalid numbers")

    @width.setter
    def width(self, width):
        if (0.0<width<20.0)  and type(width) is float:
            self.__width=width



rectangle1 = Rectangle()
rectangle1.width = 2.36
rectangle1.length = 6.32
print(rectangle1.count_area())
