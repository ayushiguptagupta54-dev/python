# #  Accesing specifie in python
class student:
        def __init__(self):
           self._name = "Ayush"

        def _funName(self):     # protected method
            return "Codewithayush"

class Subject(student):     # Inheritance class
    pass

obj = student()
obj1 = Subject()
print(dir(obj))

#  Calling by ibject of student class
print(obj._name)
print(obj._funName())
#  Calling by object od subject class
print(obj1._name)
print(obj1._funName())

