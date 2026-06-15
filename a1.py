marks = [10,20, 30, 40, 50, 60]
#  Access o(1)
print(marks[5])
print(marks[3])
print(marks[-1])
#  add to end (1)
marks.append(100)
print(marks)

#  specific position O(n)
marks.insert(2,55)
print(marks)
marks.remove(30)
print(marks)
marks.pop(3)
print(marks)
print(marks[1:4])
print(marks[::2])

