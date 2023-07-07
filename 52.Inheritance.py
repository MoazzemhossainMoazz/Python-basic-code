#Parent class = Super class = Base class
#Child class = sub class = Derived class
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class Samsung:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

    def photo(self):
        print("You can take photo")

p = Phone()
p.message()
p.call()

s = Samsung()
s.message()
s.call()
s.photo()

#another way
print("Another way: ")

class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class Samsung(Phone): #call, message
    def photo(self):
        print("You can take photo")

s = Samsung()
s.message()
s.call()
s.photo()