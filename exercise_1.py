<<<<<<< HEAD
class CarClass:

    def __init__(self, model, color, currspeed, maxSpeed):
        self.model = model
        self.color = color
        self.currspeed = currspeed
        self.maxSpeed = maxSpeed


    def changeSpeed(self, amount):
        newSpeed = self.currspeed + amount
        if newSpeed >= self.maxSpeed:
            self.currspeed = self.maxSpeed
        elif newSpeed <=0:
            self.currspeed = 0
        else:
            self.currspeed = newSpeed

    def move(self, miles):
        fuelNeeded = miles/self.mpg
        currFuel = self.currFuel
        if currFuel <= fuelNeeded:
            self.currFuel = 0
            self.mileage = self.mileage + currFuel * self.mpg
            print("Warning: out of fuel")

        else:
            self.currFuel = currFuel - fuelNeeded
            self.mileage = self.mileage + miles

car = CarClass("Ferrari", "yellow", 0, 200)
car1 = car
print(car1.maxSpeed)
=======
class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return accelerate()

    def brake(self):
        self.__speed -= 5
        return brake()

    def get_speed(self):
        return self.__speed
    

    my_car = car.Car(2015, "Vauxhall")
>>>>>>> 0b84778a3658bf655b726ba595e9457aa2873eb2
