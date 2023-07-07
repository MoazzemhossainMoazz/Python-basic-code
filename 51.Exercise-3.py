class triangle:
    l = ""
    h = ""

    def set_value(self, l, h):
        self.l = l
        self.h = h

    def calculate_area(self):
        area = .5 * self.l * self.h
        print("Area = ", area)

    def display(self):
        print(f"land: {self.l}, height: {self.h}")

triangle1 = triangle()
triangle1.set_value(6,7)
triangle1.display()
triangle1.calculate_area()

print("For triangle2: ")

triangle2 = triangle()
triangle2.set_value(7,8)
triangle2.display()
triangle2.calculate_area()