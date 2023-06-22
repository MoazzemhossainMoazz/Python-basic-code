subjects = ["C", "C++", "Java", "Python", "Basic", "Dart"]
subjects.append("HTML")
print(subjects)

subjects.remove("Basic")
print(subjects)

subjects.sort()
print(subjects)

print("For number")
numbers = [4, 5, 2, 1, 7, 6]
print(4, 5, 2, 1, 7, 6)
print("After reverse")
numbers.reverse()
print(numbers)

print("After sorting")
numbers.sort()
print(numbers)

print("After reverse")
numbers.reverse()
print(numbers)

print("After pop")
numbers.pop()
print(numbers)

print("After copy list")
numbers2 = numbers.copy()
print(numbers2)

print("Find index position")
pos = numbers.index(6)
print(pos)

print("Added a value")
numbers.append(6)
print(numbers)

print("After count")
cont = numbers.count(6)
print(cont)