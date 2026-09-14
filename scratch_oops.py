class counter:
    def __init__(self,start =0):
        self.count = start

    def increment(self):
        self.count += 1

    def __repr__(self):
        return f"Counter({self.count})"
    

c1 = counter()
c2 = counter(start=10)

c1.increment()
c1.increment()
c2.increment()

print(c1)  # Output: Counter(2)
print(c2)  # Output: Counter(11)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        
    def describe(self):
        return f"{self.brand} is moving at {self.speed} km/h"
    
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"
    
class SportsCar(Car):
    def accelerate(self, amount):
        super().accelerate(amount * 2)
        
car = Car("Toyota", 4)

car.accelerate(50)
print(car.describe())  # Output: Toyota is moving at 50 km/h
print(car.honk())      # Output: Beep beep!

sports_car = SportsCar("Ferrari", 2)
print(sports_car.describe())
sports_car.accelerate(50)
print(sports_car.describe())  # Output: Ferrari is moving at 100 km/h
