class Rectangle:
    def __init__(self, width, length):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return self.width*2+self.length*2
    
        
rectangle1=Rectangle(2,2)
rectangle2=Rectangle(2,3)

print(rectangle1.area(),rectangle2.area() )
print(rectangle1.perimeter(),rectangle2.perimeter() )