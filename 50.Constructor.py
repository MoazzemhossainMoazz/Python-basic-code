class student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):   #constructor
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = student(3001, 3.67)
rahim.display()

karim = student(3002, 3.55)
karim.display()