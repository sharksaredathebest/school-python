class Car:

    def __init__(self, v, e):
        self.__VehicleID = v
        self.__Registration = None
        self.__Date0fRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    def SetPurchasePrice (self, p):
        self.__PurchasePrice = p

    def SetRegistration (self, i):
        self.__Registration = i

    def SetDateOfRegistration(self, d):
        self.__Date0fRegistration = d

    def GetVehicleID (self):
        return self.__VehicleID

    def GetRegistration (self  ):
        return self.__Registration

    def GetDate0fRegistration (self) :
        return self.__Date0fRegistration

    def GetEngineSize (self) :
        return self.__EngineSize

    def GetPurchasePrice (self) :
        return self.__PurchasePrice

car1 = Car("A12345", "3600")
car1.SetPurchasePrice(10000)
car2 = Car("B12345", "2400")
car2.SetPurchasePrice(4000)
car3 = Car("C12345", "2400")
car3.SetPurchasePrice(5000)
car4 = Car("D12345", "1444")
car4.SetPurchasePrice(6000)
car5 = Car("E12345", "2400")
car5.SetPurchasePrice(7000)



# find da cheapest
"""if cheapest > car1.GetPurchasePrice():
    cheap = car1
    cheapest = car1.GetPurchasePrice()
if cheapest > car2.GetPurchasePrice():
    cheap = car2
    cheapest = car2.GetPurchasePrice()
if cheapest > car3.GetPurchasePrice():
    cheap = car3
    cheapest = car3.GetPurchasePrice()
if cheapest > car4.GetPurchasePrice():
    cheap = car4
    cheapest = car4.GetPurchasePrice()
if cheapest > car5.GetPurchasePrice():
    cheap = car5
    cheapest = car5.GetPurchasePrice()

print(cheap.GetVehicleID())
print(cheapest)

# find da most expensive

if expensive < car1.GetPurchasePrice():
    expen = car1
    expensive = car1.GetPurchasePrice()
if expensive < car2.GetPurchasePrice():
    expen = car2
    expensive = car2.GetPurchasePrice()
if expensive < car3.GetPurchasePrice():
    expen = car3
    expensive = car3.GetPurchasePrice()
if expensive < car4.GetPurchasePrice():
    expen = car4
    expensive = car4.GetPurchasePrice()
if expensive < car5.GetPurchasePrice():
    expen = car5
    expensive = car5.GetPurchasePrice()

print(expen.GetVehicleID())
print(expensive)"""

cheapest = 10000000000000
expensive = 0

cheap = "car1"
expen = "car2"

# now do the same shit with lists
"""cars = [car1, car2, car3, car4, car5]
for i in cars:
    if i.GetPurchasePrice() < cheapest:
        cheapest = i.GetPurchasePrice()
        cheap = i.GetVehicleID()
    if i.GetPurchasePrice() > expensive:
        expensive = i.GetPurchasePrice()
        expen = i.GetVehicleID()
print("Cheapest price: ", cheapest)
print("Cheapest Vehicle: ", cheap)
print("Expensive price: ", expensive)
print("Expensivest Vehicle: ", expen)"""


# AGAIN but now user enters the values
cars = []
a = int(input("Enter the number of cars you would like to enter: "))
for i in range(a):
    car_id = input("Enter car id: ")
    car_engine = input("Enter car engine size: ")
    cars.append(Car(car_id, car_engine))
    car_price = int(input("Enter car price: "))
    cars[i].SetPurchasePrice(car_price)

for b in range(len(cars)):
    print(cars[b].GetVehicleID())

biggest = cars[0]

for f in cars:
    if f.GetEngineSize() < biggest.GetEngineSize():
        biggest = cars[f]
print("Biggest car's vehicle ID: ", biggest.GetVehicleID())
print("Biggest car's engine size: ", biggest.GetEngineSize())