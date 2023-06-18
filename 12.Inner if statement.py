# inner same as nasted loop

if 7 > 3:
   if 7 > 5:
       print("True")
   else:
        print("False")


if 7 > 3:
   if 7 > 9:
       print("True")
   else:
        print("False")


# find greatest number

num1 = 50
num2 = 30
num3 = 40

if num1 > num2:
    if num1 > num3:
        print("num1")
    else:
        print("num3")

if num2 > num1:
    if num2 > num3:
        print("num2")
    else:
        print("num3")


#anoter way

if num1 > num2:
    if num1 > num3:
        print("num1")
    else:
        print("num3")

else:
    if num2 > num3:
        print("num2")
    else:
        print("num3")