from LLD.Design_Patterns.Creational.FactoryDesignPattern.Vehicle import Vehicle


class Auto(Vehicle):

    def create(self):
        print("Creating Auto")
        return True
