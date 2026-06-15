# DEMONSTRATE INHERITANCE USING ANIMAL AND DOG CLASSESS.
class Animal:
    def sound(self):
        print("Animal make sounds")

class Dog(Animal):  
     def bark(self):
        print("Dog barks: woof woof")

d = Dog()
d.sound()
d.bark()
