num1 = 10
num2 = 20

if num1 > num2:
    print(num1)
else:
    print(num2)

#another way
print(num1 if num1>num2 else num2)

#use variable
max = num1 if num1>num2 else num2
print("Maximum=", max)