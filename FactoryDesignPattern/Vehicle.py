class Vehicle:

    def create(self):
        print("Creating Vehicle")
        return True

    def isFourWheeler(self, vehicle):

        if vehicle == "Bus" or vehicle == "Car":
            print("{} is a fourwheeler".format(vehicle))
            return True
        return False

