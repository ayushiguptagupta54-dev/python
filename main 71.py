# x = [1,2,3]     # list
# print(dir(x))
# print(x.__add__)
# x = (1,2,3)     #Tuple
# print(dir(x))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Ayush", 20)
print(p.__dict__)
print(help(Person))
