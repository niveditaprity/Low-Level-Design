from LLD.Design_Patterns.Creational.FactoryDesignPattern.Vehicle import Vehicle


class Car(Vehicle):
    def create(self):
        print("Creating Car")
        return True
