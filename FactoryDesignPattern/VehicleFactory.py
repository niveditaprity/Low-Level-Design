from LLD.FactoryDesignPattern.Auto import Auto
from LLD.FactoryDesignPattern.Car import Car
from LLD.FactoryDesignPattern.Bus import Bus
from LLD.FactoryDesignPattern.Vehicle import Vehicle


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
