class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self): #here use this
        print(f"Name = {self.name}, Color: {self.color}")

bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha FZS", "Red")
bike1.display()
bike2.display()


print("Another way: ")


class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self): #here use this
        return(f"Name: {self.name}, Color: {self.color}")

car1 = Car("Toyota", "Black")
car2 = Car("Tata", "White")
print(car1)
print(car2)
