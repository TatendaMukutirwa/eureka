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
