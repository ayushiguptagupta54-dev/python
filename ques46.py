# CREATE A CLASS STUDENT WITH ATTRIBUTES NAME AND MARKS.
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
            print("Name:", self.name)
            print("Marks:", self.marks)

s1 = student("Ayushiv", 98)
s1.display()

