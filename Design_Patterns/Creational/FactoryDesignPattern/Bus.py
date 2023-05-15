from LLD.Design_Patterns.Creational.FactoryDesignPattern.Vehicle import Vehicle


class Bus(Vehicle):

    def create(self):
        print("Creating Bus")
        return True
