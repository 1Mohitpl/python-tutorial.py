class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
    
    def full_name(self):                          #add method to the car class displays the full name of the car
        return f"{self.Brand} {self.Model}"

class ElectricCar(Car):
    def __init___(self, Brand,Model,battery_life):
        super().__init__(Brand,Model)                 #inheritance 
        self.battery_life = battery_life

my_tesla = ElectricCar("Tesla" , "modelv")
print(my_tesla.Brand)
print(my_tesla.Model)
print(my_tesla.full_name())

my_car = Car("Mahindra", "Thar")                 #create a car class with attributes like brand and model
print (my_car.Brand)

print(my_car.Model)
print(my_car.full_name())

myNew_car = Car("Tata" , "safari")
print(myNew_car.Brand)
print (myNew_car.Model)
print(myNew_car.full_name())