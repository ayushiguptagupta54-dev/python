marks = [10,20,30,40,50]
# for mark in marks:
#     print(mark)
#     for i in  range(len(marks)):
#         print(marks[i])
for mark in reversed(marks):
    print(mark)
    for mark in marks[::-1]:
        print(mark)

