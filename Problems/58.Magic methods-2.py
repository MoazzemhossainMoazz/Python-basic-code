class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return(f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = Bike("Yamaha","Blue")
bike2 = Bike("Yamaha","Blue")
print(bike1==bike2)