from LLD.FactoryDesignPattern.Vehicle import Vehicle


class Bus(Vehicle):

    def create(self):
        print("Creating Bus")
        return True
