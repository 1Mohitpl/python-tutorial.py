class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model


my_car = Car("Mahindra", "Thar")                 #create a car class with attributes like brand and model
print (my_car.Brand)

print(my_car.Model)

myNew_car = Car("Tata" , "safari")
print(myNew_car.Brand)
print (myNew_car.Model)