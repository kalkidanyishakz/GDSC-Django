from abc import ABC, abstractmethod
class Shape:
    def __init__(self, color):
       self._color=color
    
    def get_color(self):
        return self._color
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.raduis=radius
    def area(self):
        return 2*3.14*((self.raduis)**2)
    
class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
        
    
circle1=Circle('red', 3)
rectangle1=Rectangle('blue', 5,4)

print(f'''
circle color: {circle1.get_color()} circle.area {circle1.area()} circle.radius {circle1.raduis}
rectangle color: {rectangle1.get_color()} rectangle.area {rectangle1.area()} rectangle.length {rectangle1.length} rectangle.width {rectangle1.width}
      ''')