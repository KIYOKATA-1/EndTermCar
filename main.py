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

    def update(self, index, name=None, price=None, type=None, power=None):
        car = self.cars[index - 1]
        if name:
            car.name = name
        if type:
            car.type = type
        if power:
            car.power = power
        if price:
            car.price = price
        print(f"{car.name} Updated")

    def delete(self, index):
        car = self.cars.pop(index - 1)
        print(f"{car.name} Removed")

