from LLD.Design_Patterns.Creational.FactoryDesignPattern.ShapeFactory.Shape import Shape


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side