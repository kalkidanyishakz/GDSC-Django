from abc import ABC, abstractclassmethod
import math

'''
Create a class hierarchy for geometric shapes, such as "Circle," "Rectangle," and "Triangle." 
Implement a method calculate_area in each class. Demonstrate polymorphism by calling calculate_area on different shape objects.
'''

class Shape:
    def __init__(self, color):
        self.color=color
    @abstractclassmethod
    def calculate_area(self):
        pass
    

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius=radius
    
    def calculate_area(self):
        return math.pi* self.radius**2

class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)
        self.width=width
        self.length=length

    def calculate_area(self):
        return self.width*self.length


class Triangle(Shape):
    def __init__(self, color, height, base):
        super().__init__(color)
        self.height=height
        self.base=base

    def calculate_area(self):
        return (self.height*self.base)/2

    
def calculate_area(myshape):
    return myshape.calculate_area()

circle=Circle('green', 10)
rectangle=Rectangle('yellow', 5, 5)
triangle=Triangle('red', 10, 10)

print(
f'''circle: {calculate_area(circle)}
triangle: {calculate_area(triangle)}
rectangle: {calculate_area(rectangle)}'''
)