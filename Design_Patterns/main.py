from LLD.Design_Patterns.Creational.FactoryDesignPattern.ShapeFactory.ShapeFactory import ShapeFactory

shape = ShapeFactory()

circle = shape.create_shape("circle", 4)
sq = shape.create_shape("square", 4)
rectangle = shape.create_shape("rectangle", 4, 5)

print(circle.area())
print(sq.area())
print(rectangle.area())
