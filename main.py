#Create Class:
class Car:
    def __init__(self, name, price, type, power):
        self.name = name;
        self.price = price;
        self.type = type;
        self.power = power;

class CarShowRoom:
    def __init__(self):
        self.cars = []

    def add(self, name, price, type, power):
        car = Car(name, price, type, power)
        self.cars.append(car)
        print(f"{name} added")

    def read(self):
        if not self.cars:
            print("No Cars")
        for i, car in enumerate(self.cars):
            print(f"{i + 1}. {car.name} {car.type} ({car.power}) - ${car.price}")
