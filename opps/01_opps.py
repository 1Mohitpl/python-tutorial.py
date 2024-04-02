class Car:
    def __init__(self, Brand, Model):
        self.__Brand = Brand
        self.Model = Model




    def  get_brand (self):
        return self.__Brand + "!"
    
    def full_name(self):                          #add method to the car class displays the full name of the car
        return f"{self.__Brand} {self.Model}"

    def fuel_type(self):
        return "petrol or diesel"

class ElectricCar(Car):
    def __init___(self, Brand,Model,battery_life):
        super().__init__(Brand,Model)                 #inheritance 
        self.battery_life = battery_life

    def fuel_type(self):
        return "Electric charging"

my_tesla = ElectricCar("Tesla" , "modelv")
# print(my_tesla.__Brand)
print(my_tesla.Model)
print(my_tesla.full_name())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

my_car = Car("Mahindra", "Thar")                 #create a car class with attributes like brand and model
# print (my_car.Brand)

print(my_car.Model)
print(my_car.full_name())
print(my_car.get_brand())

myNew_car = Car("Tata" , "safari")
# print(myNew_car.Brand)
print (myNew_car.Model)
print(myNew_car.full_name())
print(myNew_car.get_brand())

advanture = Car("Tata", "safari")
print(advanture.fuel_type())