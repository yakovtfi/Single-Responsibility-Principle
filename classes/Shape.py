import math

class Shape:
    def arae (self):
        return NotImplementedError

class circle(Shape):
    def __init__(self,r):
        self.r=r
    def arae (self):
        return math.pi*self.r**2

class Square(Shape):
    def __init__(self,a):
        self.a=a
    def arae (self):
        return self.a

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def arae (self):
        return self.width*self.height




