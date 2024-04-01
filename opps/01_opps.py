class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
    
    def full_name(self):                          #add method to the car class displays the full name of the car
        return f"{self.Brand} {self.Model}"


my_car = Car("Mahindra", "Thar")                 #create a car class with attributes like brand and model
print (my_car.Brand)

print(my_car.Model)
print(my_car.full_name())

myNew_car = Car("Tata" , "safari")
print(myNew_car.Brand)
print (myNew_car.Model)
print(myNew_car.full_name())