#main.py

from vehiclePackage.vehicleClass import *
from vehiclePackage.hybridClass import *
from vehiclePackage.motorcycleClass import *

if __name__ == "__main__": 
    #Instantiate an object of type hybrid 
    
    myPrius = Hybrid("Hybrid", "Toyota", "Prius", 220) #Invoke the Hybrid class constructor
    
    #Invoke the print type method using the hybrid object we just created
    myPrius.printType()
    
    '''
    #Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120) #will trigger a call to the constructor
    myCorvette.printType()  #Invoking the method on the object
    
    
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    #Instantiate another Vehicle Object
    myHarley = Vehicle("Motorcycle")
    myHarley.printType()
    
    #I was a list of 3 Vehicless: Car, Boat, Spaceship
    myVehicles = [Vehicle("Toyota Camry", 150), Vehicle("Sailboat", 20), Vehicle("Falcon Heavy", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    '''
    