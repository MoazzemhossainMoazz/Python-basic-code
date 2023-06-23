num = [10, 20, 30, 40, 50]
print(num)

index = 0
n = len(num)
while index<n:
    print(num[index])
    index = index + 1

print("\nuse for loop")
for x in num:
    print(x)

print("\nsum these number use for loop")
sum = 0
for x in num:
    sum = sum + x
print(sum)