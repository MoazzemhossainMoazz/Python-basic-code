#xargs
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add(100, 40)
add(30, 40, 20)
add(40, 22, 44, 55)

#xxargs
print("\nfor xxarguments: ")


def student(id, name):
    print(id, name)


student(id=3001, name="Moazzem")

#another way for xxargs
print("\nanother way for xxarguments: ")


def student(**details):
    print(details)
    print(details["name"])


student(id=3001, name="Moazzem")

