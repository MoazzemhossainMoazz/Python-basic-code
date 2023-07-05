"""
num2 = int(input("Enter a number: "))
result = 20/num2
print(result)
print("Done")

#
text ="Moazz"
print(text[4])
print("Done")
"""

try:
    list = [20, 0, 30]
    result = list[0] / list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible.")
except IndexError:
    print("Index error")

finally:
    print("Successful.")