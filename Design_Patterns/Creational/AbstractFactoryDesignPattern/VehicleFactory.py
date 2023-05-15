from abc import ABC, abstractmethod


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_bus(self):
        pass


class Car(ABC):
    @abstractmethod
    def create(self):
        pass


class Bus(ABC):
    @abstractmethod
    def create(self):
        pass


class ToytaFactory(Car):
    def create(self):
        print("Toyta is created")


class SumoFactory(Car):
    def create(self):
        print("Sumo is created")


class MiniBus(Bus):
    def create(self):
        print("Minibus is created")


class PartyBus(Bus):
    def create(self):
        print("Party Bus is created")


class CarVehicleFactory(VehicleFactory):
    def create_car(self, car_type):
        if car_type == "Toyota":
            return ToytaFactory()
        elif car_type == "Sumo":
            return SumoFactory()
        else:
            raise ValueError("Invalid car type.")

    def create_bus(self, bus_type):
        raise ValueError("This factory does not produce buses.")


class BusVehicleFactory(VehicleFactory):
    def create_car(self, car_type):
        raise ValueError("This factory does not produce cars.")

    def create_bus(self, bus_type):
        if bus_type == "Mini":
            return MiniBus()
        elif bus_type == "Party":
            return PartyBus()
        else:
            raise ValueError("Invalid bus type.")


def create_carvehicles(factory):
    car1 = factory.create_car("Toyota")
    car1.create()
    car2 = factory.create_car("Sumo")
    car2.create()
def create_busvehicles(factory):
    bus1 = factory.create_bus("Mini")
    bus1.create()
    bus2 = factory.create_bus("Party")
    bus2.create()



# Usage
factory1 = CarVehicleFactory()
create_carvehicles(factory1)

factory2 = BusVehicleFactory()
create_busvehicles(factory2)
