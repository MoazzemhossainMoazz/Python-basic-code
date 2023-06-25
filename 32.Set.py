num1 = {1, 2, 3, 4, 5, 5, 4} #duplidate values are not allowed in set
print(num1)

num1 = {1, 2, 3, 4, 5}
num2 = set([4, 5, 6])
print(num2)
num2.add(7)
print(7 in num2)
print(num2)
num2.remove(7)
print(num2)
print(7 in num2)

#union operation
print("union:", num1 | num2)
#intersection
print("intersection:", num1 & num2)
#difference
print("difference:", num1 - num2)
