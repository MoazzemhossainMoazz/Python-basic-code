class student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = student()
rahim.roll = 101
rahim.gpa = 4.00
rahim.display()

karim = student()
karim.roll = 102
karim.gpa = 3.45
karim.display()

#use function/Methods
print("Another way: ")

class student2:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa): #make a function/Method
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

fahim = student2() #object
fahim.set_value(105, 3.56)
fahim.display()

asif = student2() #object
asif.set_value(106, 3.78)
asif.display()