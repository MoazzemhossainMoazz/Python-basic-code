# 10 20 30 40
n = input("Enter a text of numbers: ")

list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)