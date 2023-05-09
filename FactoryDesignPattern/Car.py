from LLD.FactoryDesignPattern.Vehicle import Vehicle


class Car(Vehicle):
    def create(self):
        print("Creating Car")
        return True
