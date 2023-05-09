from abc import ABC, abstractmethod
import math


class Shape:

    @abstractmethod
    def area(self):
        print("Find Area of the shape")
        pass

    @abstractmethod
    def perimeter(self):
        print("Find perimeter of the shape")
        pass
