#use break statement
i = 1
while i <= 100:
    print(i)
    i = i+1
    if i == 20:
        break
print("here number is 1 to 19")

#use continue statement
j = 1
while j <= 30:

    j = j+1
    if j == 24:
        continue
    print(j)
print("here 24 is missing")
