class triangle:
    base = ""
    height = ""


    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        self.triangle = .5 * self.base * self.height #area = .5 * self.base * self.height
        print(f"Base: {self.base}, Height: {self.height}, Area: {self.triangle}")

    def display(self):
        print(f"Base: {self.base}, Height: {self.height}, Area: {self.triangle}")

triangle1 = triangle(10, 20)
triangle1.calculate_area()
triangle1.display()

print("for triangle2: ")

triangle2 = triangle(20, 30)
triangle2.calculate_area()
triangle2.display()


