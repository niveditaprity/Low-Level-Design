from LLD.Design_Patterns.Creational.FactoryDesignPattern.ShapeFactory.Circle import Circle
from LLD.Design_Patterns.Creational.FactoryDesignPattern.ShapeFactory.Rectangle import Rectangle
from LLD.Design_Patterns.Creational.FactoryDesignPattern.ShapeFactory.Square import Square


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'square':
            return Square(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args)
        else:
            raise ValueError('Invalid shape type')

