
import math

from LLD.FactoryDesignPattern.ShapeFactory.Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius