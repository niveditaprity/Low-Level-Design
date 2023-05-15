from LLD.Design_Patterns.Creational.FactoryDesignPattern.Auto import Auto
from LLD.Design_Patterns.Creational.FactoryDesignPattern.Car import Car
from LLD.Design_Patterns.Creational.FactoryDesignPattern.Bus import Bus
from LLD.Design_Patterns.Creational.FactoryDesignPattern.Vehicle import Vehicle


class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle):
        if vehicle == "Car":
            return Car()
        if vehicle == "Bus":
            return Bus()
        if vehicle == "Auto":
            return Auto()

        return Vehicle()
