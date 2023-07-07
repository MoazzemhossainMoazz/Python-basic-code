class phone:
    def __init__(self): #constructor/ method
        print("I am in phone class.")


class Samsung(phone):
    #init
    def __init__(self): #overriding method
        super().__init__() #super class
        print("I am in Samsung class")

s = Samsung()