#motorcycle.py

from vehiclePackage.carClass import Car; # This works but Eclipse flags an error in the editor.

class Motorcycle(Car):  #hybrid class inherits from car class
    def __init__(self, type, make, model, batteryKVA):
        self.batteryKVA = batteryKVA;
        Car.__init__(self, type, make, model);
    def printBatteryKVA(self):
        print(self.batteryKVA);