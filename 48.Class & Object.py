class student:
    roll = ""
    gpa = ""

fahim = student() #object
print(isinstance(fahim, student)) #make sure for object or not

fahim.roll = 101
fahim.gpa = 3.70
print(f"Roll: {fahim.roll}, GPA: {fahim.gpa}")

rakib = student() #object
print(isinstance(rakib, student)) #make sure for object or not
rakib.roll = 102
rakib.gpa = 3.56
print(f"Roll: {rakib.roll}, GPA: {rakib.gpa}")